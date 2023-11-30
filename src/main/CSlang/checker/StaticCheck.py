# from main.CSlang.utils.AST import *
# from main.CSlang.utils.Visitor import *
# from main.CSlang.utils.Utils import *
from typing import Optional, Callable

from AST import *
from Visitor import *
from Utils import MType

from StaticError import *
from functools import reduce

class NullType(Type):
    pass


class ReturnType:
    def __init__(self, typ, isMutable=False, scope=None):
        self.typ: Type = typ
        self.isMutable: bool = isMutable
        self.scope = scope


class Member:
    def __init__(self,n,t,isMutable=False):
        self.name: str = n
        self.typ: Type = t
        self.isMu: bool = isMutable
    def __str__(self):
        return "Member("+self.name+","+str(self.typ)+","+str(self.isMu)+")"
    def __hash__(self):
        return hash(self.name)
    def __eq__(self, other):
        return hash(self.name) == hash(other.name)
    # def __repr__(self):
    #     name = self.name
    #     typ = self.typ
    #     typ_string = f"typ={typ}" if type(typ) is MType else ""
    #     return f"Member(name={name},{typ_string})"


class BKClass:
    def __init__(self,n,p,m):
        self.name: str = n
        self.parent: str = p
        self.member: List[Member] = m
    def __str__(self):
        return "Class("+self.name+","+(self.parent if type(self.parent) == str else "None" if self.parent is None else self.parent.name)+",["+",".join(str(i) for i in self.member) +"])"


GLOBAL_ENV = [
    BKClass("io",None,[
        Member("@readInt",MType([],IntType()),False),
        Member("@readFloat",MType([],FloatType()),False),
        Member("@readBool",MType([],BoolType()),False),
        Member("@readStr",MType([],StringType()),False),
        Member("@writeInt",MType([IntType()],VoidType()),False),
        Member("@writeFloat",MType([FloatType()],VoidType()),False),
        Member("@writeBool",MType([BoolType()],VoidType()),False),
        Member("@writeStr",MType([StringType()],VoidType()),False),
    ])
]

class SymmbolLookup:
    @staticmethod
    def lookup(name: str, lst: list, typ, func: Callable):
        for x in lst:
            if name == func(x) and issubclass(type(x), typ):
                return x
        return None

    def findBKClass(self,name: str) -> Optional[BKClass]:
        return self.lookup(name, self.GLOBAL_SCOPE, BKClass, lambda x: x.name)

    @staticmethod
    def findMethods(name: str, members: List[Member]) -> List[Member]:
        return list(filter(lambda x: x.name == name and type(x.typ) == MType, members))

class TypeChecker:
    def typeCoerce(self, ast, lhsType, rhsType):
        if self.checkTypeRightToLeft(lhsType, rhsType):
            return self.typeCoerceRightToLeft(ast, lhsType, rhsType)
        if self.checkTypeRightToLeft(rhsType, lhsType):
            return self.typeCoerceRightToLeft(ast, rhsType, lhsType)

    def typeCoerceRightToLeft(self, ast, lhsType, rhsType):
        if type(rhsType) == ReturnType:
            rhsType = rhsType.typ
        if type(lhsType) == ReturnType:
            lhsType = lhsType.typ
        if not self.checkTypeRightToLeft(lhsType, rhsType):
            raise TypeMismatchInExpression(ast)
        if type(lhsType) == type(rhsType) and type(lhsType) == ClassType:
            if self.checkClassType(lhsType, rhsType):
                return rhsType
        if type(lhsType) == type(rhsType) and type(lhsType) in [IntType, FloatType, BoolType, ArrayType, StringType]:
            return lhsType
        if type(lhsType) is FloatType and type(rhsType) is IntType:
            return lhsType
        if type(lhsType) is ClassType and type(rhsType) is NullType:
            return lhsType
        raise TypeMismatchInExpression(ast)


    def checkTypeRightToLeft(self, lhsType: Type, rhsType: Type):
        if type(rhsType) == ReturnType:
            rhsType = rhsType.typ
        if type(lhsType) == ReturnType:
            lhsType = lhsType.typ
        if type(lhsType) in [VoidType, NullType]:
            return False
        if type(lhsType) is ClassType and type(rhsType) is NullType:
            return True
        if type(lhsType) is type(rhsType) and type(lhsType) is ClassType:
            return self.checkClassType(lhsType, rhsType)
        if type(lhsType) is type(rhsType) and type(lhsType) is ArrayType:
            return self.checkArrayType(lhsType, rhsType)
        if type(lhsType) is FloatType and type(rhsType) is IntType:
            return True
        if type(lhsType) is type(rhsType):
            return True
        return False

    def checkArrayType(self, lhsType: ArrayType, rhsType: ArrayType)-> bool:
        return lhsType.size == rhsType.size and self.checkTypeRightToLeft(lhsType.eleType, rhsType.eleType)

    def checkClassType(self, lhsType: ClassType, rhsType: ClassType):
        if lhsType.classname == rhsType.classname or self.checkClassTypeCoerce(lhsType, rhsType):
            return True
        return False

    def checkClassTypeCoerce(self, lhs_name: ClassType, rhs_name: ClassType) -> str:
        rhs_name = rhs_name.classname.name
        while True:
            parent_class = self.PARENT_TABLE.get(rhs_name)
            if not parent_class:
                return None
            if parent_class == lhs_name.classname.name:
                return parent_class
            rhs_name = parent_class

    @staticmethod
    def isSameTypeArray(lst: List[ReturnType])-> bool:
        ele_type = type(lst[0].typ)
        for i in lst[1:]:
            if type(i.typ) != ele_type: return False
        return True

    def isValidParamsType(self, lhsParams, rhsParams)-> bool:
        return (len(lhsParams) == len(rhsParams)
                and all([self.checkTypeRightToLeft(lhs, rhs) for lhs, rhs in zip(lhsParams, rhsParams)]))


class StaticChecker(BaseVisitor, TypeChecker, SymmbolLookup):

    def _set_undeclared_check(self, a):
        self._ENABLE_UNDECLARED_CHECK = a

    def _set_traverse_method_body(self, a):
        self._ALLOW_TRAVERSE_METHOD_BODY = a


    def __init__(self,ast):
        self.ast = ast
        self.io = GLOBAL_ENV
        self.GLOBAL_SCOPE = []
        self.PARENT_TABLE = dict()
        self._ENABLE_UNDECLARED_CHECK = False
        self._ALLOW_TRAVERSE_METHOD_BODY = False
        self.CURRENT_CLASS = None
        self.CURRENT_METHOD = None
        self.IN_LOOP = 0

    def resolveInheritAttributes(self):
        for bk_class in self.GLOBAL_SCOPE:
            constructor_methods = self.findMethods('constructor', bk_class.member)
            members = set(bk_class.member) - set(constructor_methods)
            parent_name = bk_class.parent
            while True:
                if not parent_name:
                    break
                parent_class = self.findBKClass(parent_name)
                if self._ENABLE_UNDECLARED_CHECK and not parent_class:
                    raise Undeclared(Class(), parent_name)
                parent_class_member = list(filter(lambda x: x.name != 'constructor' and not x.name.startswith("@"), parent_class.member))
                members.update(parent_class_member)
                parent_name = parent_class.parent
            bk_class.member = list(members) + constructor_methods

    def check_entry_point(self):
        program_class: BKClass = SymmbolLookup.lookup("Program", self.GLOBAL_SCOPE, BKClass, lambda x: x.name)
        if program_class:
            main_method: Member = self.lookup("@main", program_class.member, Member, lambda x: x.name)
            if main_method and main_method.typ == MType([],VoidType()):
                return
        raise NoEntryPoint()

    def check(self):
        self._set_traverse_method_body(False)
        scope = self.visit(self.ast, self.io)
        self.GLOBAL_SCOPE = scope
        self._set_undeclared_check(True)
        self.resolveInheritAttributes()
        self._set_traverse_method_body(True)
        self.visit(self.ast, [])
        self.check_entry_point()
        return "successful"

    def visitProgram(self, ast: Program, scope):
        return reduce(lambda a, e: self.visit(e, a), ast.decl, scope)

    def visitClassDecl(self, ast: ClassDecl, scope):
        parent_name = ast.parentname.name if ast.parentname else None
        name = ast.classname.name
        if name in map(lambda x: x.name, scope):
            raise Redeclared(Class(), name)
        elif not self._ENABLE_UNDECLARED_CHECK and ast.parentname:
            self.PARENT_TABLE[ast.classname.name] = str(ast.parentname.name)
        if self._ALLOW_TRAVERSE_METHOD_BODY:
            self.CURRENT_CLASS = self.findBKClass(name)
        mem = reduce(lambda a,e: self.visit(e,a) ,ast.memlist,[])
        current_class = BKClass(name, parent_name, mem)
        return [current_class] + scope

    def visitAttributeDecl(self, ast: AttributeDecl, scope):
        try:
            return self.visit(ast.decl, scope)
        except Redeclared as exc:
            raise Redeclared(Attribute(), exc.n)

    def visitVarDecl(self, ast: VarDecl, scope):
        lhsType = self.visit(ast.varType, scope)
        member_type = lhsType
        if ast.varInit:
            rhsType: ReturnType = self.visit(ast.varInit, scope)
            try:
                member_type = self.typeCoerceRightToLeft(ast, lhsType, rhsType.typ)
            except TypeMismatchInExpression as exc:
                raise TypeMismatchInDeclaration(ast)
        if type(ast.varType) == VoidType:
            raise TypeMismatchInDeclaration(ast)
        if ast.variable.name in map(lambda x: x.name, scope):
            raise Redeclared(Variable(),ast.variable.name)
        if type(member_type) is ReturnType:
            member_type = member_type.typ
        return scope + [Member(ast.variable.name, member_type, True)]

    def visitConstDecl(self, ast: ConstDecl, scope):
        if not ast.value:
            raise TypeMismatchInDeclaration(ast)
        lhsType = self.visit(ast.constType, scope)
        rhsType: ReturnType = self.visit(ast.value, scope)
        try:
            member_type = self.typeCoerceRightToLeft(ast, lhsType, rhsType.typ)
        except TypeMismatchInExpression as exc:
            raise TypeMismatchInDeclaration(ast)
        if ast.constant.name in map(lambda x: x.name, scope):
            raise Redeclared(Constant(),ast.constant.name)
        return scope + [Member(ast.constant.name, member_type, False)]

    def visitMethodDecl(self, ast: MethodDecl, scope):
        name = ast.name.name
        if name in map(lambda x: x.name, scope) and name != "constructor":
            raise Redeclared(Method(), name)
        try:
            param_members = reduce(lambda a,c: self.visit(c, a), ast.param, [])
        except Redeclared as exc:
            raise Redeclared(Parameter(), exc.n)
        param_types = [param.typ for param in param_members]
        return_type = self.visit(ast.returnType, scope) if name != 'constructor' \
            else VoidType()
        if type(return_type) is ReturnType:
            return_type = return_type.typ
        current_method = Member(name, MType(param_types, return_type))
        if self._ALLOW_TRAVERSE_METHOD_BODY:
            self.CURRENT_METHOD = current_method
            self.visit(ast.body, param_members)
            self.CURRENT_METHOD = None
        return [current_method] + scope

    def visitBlock(self, ast, param):
        return reduce(lambda a,e: self.visit(e,a), ast.stmt, param)

    def visitClassType(self, ast: ClassType, scope):
        name = ast.classname.name
        if not self._ENABLE_UNDECLARED_CHECK:
            return ast
        class_type: BKClass = self.findBKClass(ast.classname.name)
        if not class_type:
            raise Undeclared(Class(), name)
        return ReturnType(ast, False, class_type.member)

    def visitFieldAccess(self,ast: FieldAccess,param):
        class_obj: ReturnType = self.visit(ast.obj, param + self.GLOBAL_SCOPE)
        if type(class_obj.typ) is not ClassType:
            raise TypeMismatchInExpression(ast)
        class_name: BKClass = self.findBKClass(class_obj.typ.classname.name)
        try:
            return self.visit(ast.fieldname, class_name.member)
        except Undeclared as exc:
            raise Undeclared(Attribute(), exc.n)

    def visitId(self, ast: Id, param):
        name: Member = self.lookup(ast.name, param, object, lambda x: x.name)
        if self._ENABLE_UNDECLARED_CHECK and not name:
            raise Undeclared(Identifier(), ast.name)
        if type(name) is BKClass:
            return ReturnType(ClassType(Id(name.name)), False, name.member)
        return ReturnType(name.typ, name.isMu, param)

    def visitIntType(self,ast,param):
        return ast

    def visitFloatType(self,ast,param):
        return ast

    def visitBoolType(self,ast,param):
        return ast

    def visitStringType(self,ast,param):
        return ast

    def visitVoidType(self,ast,param):
        return ast

    def visitArrayType(self,ast,param):
        return ast

    def visitIntLiteral(self, ast: IntLiteral, param):
        return ReturnType(IntType(), False)

    def visitFloatLiteral(self, ast, param):
        return ReturnType(FloatType(), False)

    def visitBooleanLiteral(self, ast, param):
        return ReturnType(BoolType(), False)

    def visitStringLiteral(self, ast, param):
        return ReturnType(StringType(), False)

    def visitNullLiteral(self, ast, param):
        return ReturnType(NullType(), False)

    def visitSelfLiteral(self, ast, param):
        current_class: BKClass = self.CURRENT_CLASS
        return ReturnType(ClassType(Id(current_class.name)), False, current_class.member)

    def visitArrayLiteral(self, ast: ArrayLiteral, param):
        element_types = [self.visit(x, param) for x in ast.value]
        if not self.isSameTypeArray(element_types):
            raise IllegalArrayLiteral(ast)
        return ReturnType(ArrayType(len(element_types),element_types[0]), False)

    def visitAssign(self, ast: Assign, param):
        lhs: ReturnType = self.visit(ast.lhs, param)
        if type(lhs.typ) in [VoidType, MType]:
            raise TypeMismatchInStatement(ast)
        rhs: ReturnType = self.visit(ast.exp, param)
        if not self.checkTypeRightToLeft(lhs.typ, rhs.typ):
            raise TypeMismatchInStatement(ast)
        if not lhs.isMutable:
            raise CannotAssignToConstant(ast)
        return param

    def visitCallStmt(self, ast: CallStmt, param):
        if not ast.method.name.startswith("@") and not ast.obj:
            raise TypeMismatchInStatement(ast)
        if ast.obj:
            try:
                current_class: ReturnType = self.visit(ast.obj, param + self.GLOBAL_SCOPE)
            except Undeclared as exc:
                if ast.method.name.startswith("@"):
                    raise Undeclared(Class(), exc.n)
                raise exc
            class_type = current_class.typ
            if type(class_type) is not ClassType:
                raise TypeMismatchInStatement(ast)
            class_name: BKClass = self.findBKClass(class_type.classname.name)
            scope = class_name.member
        else:
            scope = self.CURRENT_CLASS.member
        try:
            method: ReturnType = self.visit(ast.method, scope)
        except Undeclared as exc:
            raise Undeclared(Method(), exc.n)
        method_type = method.typ
        if type(method_type) is not MType or not type(method_type.rettype) is VoidType:
            raise TypeMismatchInStatement(ast)
        params = list(map(lambda x: self.visit(x, param), ast.param))
        if not self.isValidParamsType(method_type.partype, params):
            raise TypeMismatchInStatement(ast)
        return param

    def visitBinaryOp(self, ast: BinaryOp, param):
        lhs: ReturnType = self.visit(ast.left, param)
        rhs: ReturnType = self.visit(ast.right, param)
        type_lhs = type(lhs.typ)
        type_rhs = type(rhs.typ)
        returnType = None
        if ast.op == '^' \
                and type_lhs is StringType \
                and type_rhs is StringType:
            returnType = StringType()
        elif ast.op in ['+', '-', '*'] \
                and type_lhs in [FloatType, IntType] \
                and type_rhs in [FloatType, IntType]:
            returnType = self.typeCoerce(ast, lhs, rhs)
        elif ast.op == '/' \
                and type_lhs is FloatType \
                and type_rhs is FloatType:
            returnType = FloatType()
        elif ast.op in ['\\', '%'] \
            and type_lhs is IntType \
            and type_rhs is IntType:
            returnType = IntType()
        elif ast.op in ['<', '<=', '>', '>='] \
            and type_lhs in [FloatType, IntType] \
            and type_rhs in [FloatType, IntType]:
            returnType = BoolType()
        elif ast.op in ['==', '!='] \
            and type_lhs in [BoolType, IntType] \
            and type_rhs in [BoolType, IntType]:
            returnType = BoolType()
        elif ast.op in ['&&', '||'] \
            and type_lhs is BoolType \
            and type_rhs is BoolType:
            returnType = BoolType()
        if returnType:
            return ReturnType(returnType, False)
        raise TypeMismatchInExpression(ast)

    def visitUnaryOp(self, ast: UnaryOp, param):
        exp = self.visit(ast.body, param)
        exp_type = type(exp.typ)
        returnType = None
        if ast.op in ['+', '-'] and exp_type in [FloatType, IntType]:
            return ReturnType(exp.typ, False)
        elif ast.op == '!' and exp_type is BoolType:
            return ReturnType(exp.typ, False)
        raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast: CallExpr, param):
        if not ast.method.name.startswith("@") and not ast.obj:
            raise TypeMismatchInExpression(ast)
        if ast.obj:
            try:
                current_class: ReturnType = self.visit(ast.obj, param + self.GLOBAL_SCOPE)
            except Undeclared as exc:
                if ast.method.name.startswith("@"):
                    raise Undeclared(Class(), exc.n)
                raise exc
            class_type = current_class.typ
            if type(class_type) is not ClassType:
                raise TypeMismatchInExpression(ast)
            class_name: BKClass = self.findBKClass(class_type.classname.name)
            scope = class_name.member
        else:
            scope = self.CURRENT_CLASS.member

        try:
            method: ReturnType = self.visit(ast.method, scope)
        except Undeclared as exc:
            raise Undeclared(Method(), exc.n)
        method_type = method.typ
        if type(method_type) is not MType or type(method_type.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)
        params = list(map(lambda x: self.visit(x, param), ast.param))
        if not self.isValidParamsType(method_type.partype, params):
            raise TypeMismatchInExpression(ast)
        return ReturnType(method_type.rettype, False)

    def visitNewExpr(self, ast: NewExpr, param):
        bk_class: BKClass = self.findBKClass(ast.classname.name)
        if not bk_class:
            raise Undeclared(Class(), ast.classname.name)
        constructor_methods = self.findMethods("constructor", bk_class.member)
        if not constructor_methods:
            raise TypeMismatchInExpression(ast)
        params = list(map(lambda x: self.visit(x, param), ast.param))
        for constructor_method in constructor_methods:
            if self.isValidParamsType(constructor_method.typ.partype, params):
                return ReturnType(ClassType(ast.classname), False, bk_class.member)
        raise TypeMismatchInExpression(ast)

    def visitArrayCell(self, ast: ArrayCell, param):
        arr: ReturnType = self.visit(ast.arr, param)
        idx: ReturnType = self.visit(ast.idx, param)
        if type(idx.typ) is not IntType or type(arr.typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        return ReturnType(arr.typ.eleType, True)

    def visitIf(self, ast: If, param):
        expr: ReturnType = self.visit(ast.expr, param)
        if type(expr.typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        if ast.preStmt:
            param = self.visit(ast.preStmt, param)
        self.visit(ast.thenStmt, param)
        if ast.elseStmt:
            self.visit(ast.elseStmt, param)
        return param

    def visitFor(self, ast: For, param):
        expr: ReturnType = self.visit(ast.expr, param)
        if type(expr.typ) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.initStmt, param)
        self.visit(ast.postStmt, param)
        self.IN_LOOP += 1
        self.visit(ast.loop, param)
        self.IN_LOOP -= 1
        return param

    def visitContinue(self, ast, param):
        if not self.IN_LOOP:
            raise MustInLoop(ast)
        return param

    def visitBreak(self, ast, param):
        if not self.IN_LOOP:
            raise MustInLoop(ast)
        return param

    def visitReturn(self, ast: Return, param):
        current_method: Member = self.CURRENT_METHOD
        current_method_rettype = current_method.typ.rettype
        if ast.expr:
            expr: ReturnType = self.visit(ast.expr, param)
            expr_type = expr.typ
        else:
            expr_type = VoidType()
        if type(current_method_rettype) is type(expr_type) and type(current_method_rettype) is VoidType:
            return param
        if self.checkTypeRightToLeft(current_method_rettype, expr_type):
            return param
        raise TypeMismatchInStatement(ast)
