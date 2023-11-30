from CSlangVisitor import CSlangVisitor
from CSlangParser import CSlangParser
# from AST import *
# from AST_org import *

from main.CSlang.utils.AST import *

import collections
def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

class ASTGeneration(CSlangVisitor):

    def visitProgram(self,ctx):
        return Program([self.visit(x) for x in ctx.classDecl()])

    def visitClassDecl(self,ctx):
        stmts = self.visit(ctx.classStmtsNullable())
        if len(ctx.idLit()) == 1:
            class_id = self.visit(ctx.idLit(0))
            return ClassDecl(class_id, stmts)
        else:
            class_id = self.visit(ctx.idLit(1))
            parent_id = self.visit(ctx.idLit(0))
            return ClassDecl(class_id, stmts, parent_id)

    def visitConstructorDecl(self, ctx):
        id = Id('constructor')
        block = self.visit(ctx.blockStmt())
        vardecls = self.visit(ctx.listDeclParams())
        return MethodDecl(id, vardecls, VoidType(), block)

    def visitClassStmtsNullable(self, ctx):
        return flatten([self.visit(x) for x in ctx.classStmt()])

    def visitClassStmt(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitAttributeStmt(self, ctx):
        decls = self.visit(ctx.getChild(0))
        return [AttributeDecl(decl) for decl in decls]

    def visitSingleDeclParam(self, ctx):
        id = self.visit(ctx.idLit())
        varType = self.visit(ctx.varType())
        return VarDecl(id, varType)

    def visitDeclParams(self, ctx):
        ids = self.visit(ctx.listIds())
        varType = self.visit(ctx.varType())
        return [VarDecl(x, varType) for x in ids]

    def visitListDeclParams(self, ctx):
        if not ctx.declParams():
            return []
        declParams = flatten([self.visit(x) for x in ctx.declParams()])
        if ctx.singleDeclParam():
            declParams.append(self.visit(ctx.singleDeclParam()))
        return declParams

    def visitMethodDecl(self, ctx):
        id = self.visit(ctx.mixedId())
        vardecls = self.visit(ctx.listDeclParams())
        return_type = self.visit(ctx.varType())
        block = self.visit(ctx.blockStmt())
        return MethodDecl(id, vardecls, return_type, block)

    def visitIdLit(self,ctx):
        return Id(ctx.ID().getText())

    def visitStaticId(self,ctx):
        return Id(ctx.STATIC_ID().getText())

    def visitMixedId(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitLiteral(self, ctx):
        value = ctx.getChild(0).getText()
        if ctx.INTLIT():
            return IntLiteral(int(value))
        if ctx.FLOATLIT():
            return FloatLiteral(float(value))
        if ctx.STRINGLIT():
            return StringLiteral(value)
        return self.visit(ctx.getChild(0))

    def visitVariableLit(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitIndexedArrayLit(self, ctx):
        exps = self.visit(ctx.listExps())
        return ArrayLiteral(exps)

    def visitNullLit(self, ctx):
        return NullLiteral()

    def visitSelfLit(self, ctx):
        return SelfLiteral()

    def visitBooleanLit(self, ctx):
        return BooleanLiteral(True) if ctx.TRUE() else BooleanLiteral(False)

    def visitPrimitiveType(self, ctx):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.STRING():
            return StringType()
        if ctx.BOOLEAN():
            return BoolType()

    def visitClassType(self, ctx):
        return ClassType(self.visit(ctx.getChild(0)))

    def visitVarType(self,ctx):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.getChild(0))


    def visitArrayType(self, ctx):
        size = int(ctx.INTLIT().getText())
        type = self.visit(ctx.primitiveType())
        return ArrayType(size, type)

    def visitExp(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return BinaryOp(op, left, right)

    def visitExp1(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return BinaryOp(op, left, right)


    def visitExp2(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return BinaryOp(op, left, right)

    def visitExp3(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return BinaryOp(op, left, right)

    def visitExp4(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return BinaryOp(op, left, right)

    def visitExp5(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        op = ctx.getChild(0).getText()
        operand = self.visit(ctx.getChild(1))
        return UnaryOp(op, operand)

    def visitOperand(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        arr = self.visit(ctx.getChild(0))
        idx = self.visit(ctx.getChild(2))
        return ArrayCell(arr, idx)

    def visitOperand1(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        obj = self.visit(ctx.getChild(0))
        fieldname = self.visit(ctx.getChild(2))
        if ctx.listParams():
            listParams = self.visit(ctx.listParams())
            return CallExpr(obj, fieldname, listParams)
        return FieldAccess(obj, fieldname)

    def visitOperand2(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        obj = None
        fieldname= self.visit(ctx.staticId())
        if ctx.DOT():
            obj = self.visit(ctx.operand3())
        if ctx.listParams():
            listParams = self.visit(ctx.listParams())
            return CallExpr(obj, fieldname, listParams)
        return FieldAccess(obj, fieldname)

    def visitOperand3(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitOperand4(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitOperand5(self, ctx):
        return self.visit(ctx.getChild(1))

    def visitListExps(self, ctx):
        return [self.visit(x) for x in ctx.exp()]

    def visitListExpsNotNull(self, ctx):
        return [self.visit(x) for x in ctx.exp()]

    def visitListParams(self, ctx):
        return self.visit(ctx.listExps())

    def visitIndexOperator(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        arr = self.visit(ctx.getChild(0))
        idx = self.visit(ctx.getChild(2))
        return ArrayCell(arr, idx)

    def visitMemberAccess(self, ctx):
        obj = self.visit(ctx.getChild(0))
        fieldname = self.visit(ctx.getChild(2))
        return FieldAccess(obj, fieldname)


    def visitStaticMemberAccess(self, ctx):
        static_id = self.visit(ctx.staticId())
        obj = self.visit(ctx.operand()) if ctx.operand() else None
        return FieldAccess(obj, static_id)

    def visitInstanceMethodInvocation(self, ctx):
        obj = self.visit(ctx.getChild(0))
        fieldname = self.visit(ctx.getChild(2))
        params = self.visit(ctx.getChild(3))
        return CallStmt(obj, fieldname, params)

    def visitStaticMethodInvocation(self, ctx):
        obj = None
        if ctx.operand():
            obj = self.visit(ctx.operand())
        fieldname = self.visit(ctx.staticId())
        params = self.visit(ctx.listParams())
        return CallStmt(obj, fieldname, params)

    def visitObjectCreation(self, ctx):
        id = self.visit(ctx.idLit())
        listParams = self.visit(ctx.listParams())
        return NewExpr(id, listParams)

    def visitListIds(self, ctx):
        return [self.visit(x) for x in ctx.idLit()]

    def visitListMixedIds(self, ctx):
        return [self.visit(x) for x in ctx.mixedId()]

    def visitVarDeclStmt(self, ctx):
        ids, var_type, init_value = self.visit(ctx.getChild(1))
        return [VarDecl(x, y, z) for x,y,z in zip(ids, var_type, init_value)]

    def visitValDeclStmt(self, ctx):
        ids, var_type, init_value = self.visit(ctx.getChild(1))
        return [ConstDecl(x, y, z) for x,y,z in zip(ids, var_type, init_value)]

    def visitDeclareWithoutAssign(self, ctx):
        ids = self.visit(ctx.listMixedIds())
        var_types = [self.visit(ctx.varType())] * len(ids)
        init_values = [None]* len(ids)
        return ids, var_types, init_values

    def visitDeclareWithAssign(self, ctx):
        if ctx.varType():
            mixed_id = self.visit(ctx.mixedId())
            var_type = self.visit(ctx.varType())
            init_value = self.visit(ctx.exp())
            return [mixed_id], [var_type], [init_value]
        mixed_ids, var_types, init_values = self.visit(ctx.declareWithAssign())
        mixed_ids.insert(0, self.visit(ctx.mixedId()))
        var_types.append(var_types[-1])
        init_values.append(self.visit(ctx.exp()))
        return mixed_ids, var_types, init_values

    def visitAssignStmt(self, ctx):
        return Assign(self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))

    def visitAssignStmtSemi(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitIfStmt(self, ctx):
        exp = self.visit(ctx.exp())
        blockStmt = self.visit(ctx.blockStmt())
        preStmt = self.visit(ctx.preStmt()) if ctx.preStmt() else None
        elseStmt = self.visit(ctx.elseStmt()) if ctx.elseStmt() else None
        return If(exp, blockStmt, preStmt, elseStmt)

    def visitPreStmt(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitElseStmt(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitForStmt(self, ctx):
        initStmt = self.visit(ctx.assignStmt(0))
        exp = self.visit(ctx.exp())
        iterStmt = self.visit(ctx.assignStmt(1))
        blockStmt = self.visit(ctx.blockStmt())
        return For(initStmt, exp, iterStmt, blockStmt)

    def visitBreakStmt(self, ctx):
        return Break()

    def visitContinueStmt(self, ctx):
        return Continue()

    def visitReturnStmt(self, ctx):
        exp = self.visit(ctx.exp()) if ctx.exp() else None
        return Return(exp)

    def visitMethodInvocationStmt(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitBlockStmt(self, ctx):
        return Block(self.visit(ctx.stmts()))

    def visitStmts(self, ctx):
        if not ctx.stmt():
            return []
        return flatten([self.visit(x) for x in ctx.stmt()])

    def visitStmt(self, ctx):
        return self.visit(ctx.getChild(0))
