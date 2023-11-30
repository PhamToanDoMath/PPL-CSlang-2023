# Generated from D:/Bai tap/HL231/PPL/assignment3-initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete listener for a parse tree produced by CSlangParser.
class CSlangListener(ParseTreeListener):

    # Enter a parse tree produced by CSlangParser#program.
    def enterProgram(self, ctx:CSlangParser.ProgramContext):
        pass

    # Exit a parse tree produced by CSlangParser#program.
    def exitProgram(self, ctx:CSlangParser.ProgramContext):
        pass


    # Enter a parse tree produced by CSlangParser#classDecl.
    def enterClassDecl(self, ctx:CSlangParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#classDecl.
    def exitClassDecl(self, ctx:CSlangParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#constructorDecl.
    def enterConstructorDecl(self, ctx:CSlangParser.ConstructorDeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#constructorDecl.
    def exitConstructorDecl(self, ctx:CSlangParser.ConstructorDeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#classStmtsNullable.
    def enterClassStmtsNullable(self, ctx:CSlangParser.ClassStmtsNullableContext):
        pass

    # Exit a parse tree produced by CSlangParser#classStmtsNullable.
    def exitClassStmtsNullable(self, ctx:CSlangParser.ClassStmtsNullableContext):
        pass


    # Enter a parse tree produced by CSlangParser#classStmt.
    def enterClassStmt(self, ctx:CSlangParser.ClassStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#classStmt.
    def exitClassStmt(self, ctx:CSlangParser.ClassStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#attributeStmt.
    def enterAttributeStmt(self, ctx:CSlangParser.AttributeStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#attributeStmt.
    def exitAttributeStmt(self, ctx:CSlangParser.AttributeStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#singleDeclParam.
    def enterSingleDeclParam(self, ctx:CSlangParser.SingleDeclParamContext):
        pass

    # Exit a parse tree produced by CSlangParser#singleDeclParam.
    def exitSingleDeclParam(self, ctx:CSlangParser.SingleDeclParamContext):
        pass


    # Enter a parse tree produced by CSlangParser#declParams.
    def enterDeclParams(self, ctx:CSlangParser.DeclParamsContext):
        pass

    # Exit a parse tree produced by CSlangParser#declParams.
    def exitDeclParams(self, ctx:CSlangParser.DeclParamsContext):
        pass


    # Enter a parse tree produced by CSlangParser#listDeclParams.
    def enterListDeclParams(self, ctx:CSlangParser.ListDeclParamsContext):
        pass

    # Exit a parse tree produced by CSlangParser#listDeclParams.
    def exitListDeclParams(self, ctx:CSlangParser.ListDeclParamsContext):
        pass


    # Enter a parse tree produced by CSlangParser#methodDecl.
    def enterMethodDecl(self, ctx:CSlangParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by CSlangParser#methodDecl.
    def exitMethodDecl(self, ctx:CSlangParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by CSlangParser#idLit.
    def enterIdLit(self, ctx:CSlangParser.IdLitContext):
        pass

    # Exit a parse tree produced by CSlangParser#idLit.
    def exitIdLit(self, ctx:CSlangParser.IdLitContext):
        pass


    # Enter a parse tree produced by CSlangParser#staticId.
    def enterStaticId(self, ctx:CSlangParser.StaticIdContext):
        pass

    # Exit a parse tree produced by CSlangParser#staticId.
    def exitStaticId(self, ctx:CSlangParser.StaticIdContext):
        pass


    # Enter a parse tree produced by CSlangParser#mixedId.
    def enterMixedId(self, ctx:CSlangParser.MixedIdContext):
        pass

    # Exit a parse tree produced by CSlangParser#mixedId.
    def exitMixedId(self, ctx:CSlangParser.MixedIdContext):
        pass


    # Enter a parse tree produced by CSlangParser#literal.
    def enterLiteral(self, ctx:CSlangParser.LiteralContext):
        pass

    # Exit a parse tree produced by CSlangParser#literal.
    def exitLiteral(self, ctx:CSlangParser.LiteralContext):
        pass


    # Enter a parse tree produced by CSlangParser#variableLit.
    def enterVariableLit(self, ctx:CSlangParser.VariableLitContext):
        pass

    # Exit a parse tree produced by CSlangParser#variableLit.
    def exitVariableLit(self, ctx:CSlangParser.VariableLitContext):
        pass


    # Enter a parse tree produced by CSlangParser#indexedArrayLit.
    def enterIndexedArrayLit(self, ctx:CSlangParser.IndexedArrayLitContext):
        pass

    # Exit a parse tree produced by CSlangParser#indexedArrayLit.
    def exitIndexedArrayLit(self, ctx:CSlangParser.IndexedArrayLitContext):
        pass


    # Enter a parse tree produced by CSlangParser#nullLit.
    def enterNullLit(self, ctx:CSlangParser.NullLitContext):
        pass

    # Exit a parse tree produced by CSlangParser#nullLit.
    def exitNullLit(self, ctx:CSlangParser.NullLitContext):
        pass


    # Enter a parse tree produced by CSlangParser#selfLit.
    def enterSelfLit(self, ctx:CSlangParser.SelfLitContext):
        pass

    # Exit a parse tree produced by CSlangParser#selfLit.
    def exitSelfLit(self, ctx:CSlangParser.SelfLitContext):
        pass


    # Enter a parse tree produced by CSlangParser#booleanLit.
    def enterBooleanLit(self, ctx:CSlangParser.BooleanLitContext):
        pass

    # Exit a parse tree produced by CSlangParser#booleanLit.
    def exitBooleanLit(self, ctx:CSlangParser.BooleanLitContext):
        pass


    # Enter a parse tree produced by CSlangParser#primitiveType.
    def enterPrimitiveType(self, ctx:CSlangParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by CSlangParser#primitiveType.
    def exitPrimitiveType(self, ctx:CSlangParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by CSlangParser#classType.
    def enterClassType(self, ctx:CSlangParser.ClassTypeContext):
        pass

    # Exit a parse tree produced by CSlangParser#classType.
    def exitClassType(self, ctx:CSlangParser.ClassTypeContext):
        pass


    # Enter a parse tree produced by CSlangParser#varType.
    def enterVarType(self, ctx:CSlangParser.VarTypeContext):
        pass

    # Exit a parse tree produced by CSlangParser#varType.
    def exitVarType(self, ctx:CSlangParser.VarTypeContext):
        pass


    # Enter a parse tree produced by CSlangParser#arrayType.
    def enterArrayType(self, ctx:CSlangParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by CSlangParser#arrayType.
    def exitArrayType(self, ctx:CSlangParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by CSlangParser#exp.
    def enterExp(self, ctx:CSlangParser.ExpContext):
        pass

    # Exit a parse tree produced by CSlangParser#exp.
    def exitExp(self, ctx:CSlangParser.ExpContext):
        pass


    # Enter a parse tree produced by CSlangParser#exp1.
    def enterExp1(self, ctx:CSlangParser.Exp1Context):
        pass

    # Exit a parse tree produced by CSlangParser#exp1.
    def exitExp1(self, ctx:CSlangParser.Exp1Context):
        pass


    # Enter a parse tree produced by CSlangParser#exp2.
    def enterExp2(self, ctx:CSlangParser.Exp2Context):
        pass

    # Exit a parse tree produced by CSlangParser#exp2.
    def exitExp2(self, ctx:CSlangParser.Exp2Context):
        pass


    # Enter a parse tree produced by CSlangParser#exp3.
    def enterExp3(self, ctx:CSlangParser.Exp3Context):
        pass

    # Exit a parse tree produced by CSlangParser#exp3.
    def exitExp3(self, ctx:CSlangParser.Exp3Context):
        pass


    # Enter a parse tree produced by CSlangParser#exp4.
    def enterExp4(self, ctx:CSlangParser.Exp4Context):
        pass

    # Exit a parse tree produced by CSlangParser#exp4.
    def exitExp4(self, ctx:CSlangParser.Exp4Context):
        pass


    # Enter a parse tree produced by CSlangParser#exp5.
    def enterExp5(self, ctx:CSlangParser.Exp5Context):
        pass

    # Exit a parse tree produced by CSlangParser#exp5.
    def exitExp5(self, ctx:CSlangParser.Exp5Context):
        pass


    # Enter a parse tree produced by CSlangParser#operand.
    def enterOperand(self, ctx:CSlangParser.OperandContext):
        pass

    # Exit a parse tree produced by CSlangParser#operand.
    def exitOperand(self, ctx:CSlangParser.OperandContext):
        pass


    # Enter a parse tree produced by CSlangParser#operand1.
    def enterOperand1(self, ctx:CSlangParser.Operand1Context):
        pass

    # Exit a parse tree produced by CSlangParser#operand1.
    def exitOperand1(self, ctx:CSlangParser.Operand1Context):
        pass


    # Enter a parse tree produced by CSlangParser#operand2.
    def enterOperand2(self, ctx:CSlangParser.Operand2Context):
        pass

    # Exit a parse tree produced by CSlangParser#operand2.
    def exitOperand2(self, ctx:CSlangParser.Operand2Context):
        pass


    # Enter a parse tree produced by CSlangParser#operand3.
    def enterOperand3(self, ctx:CSlangParser.Operand3Context):
        pass

    # Exit a parse tree produced by CSlangParser#operand3.
    def exitOperand3(self, ctx:CSlangParser.Operand3Context):
        pass


    # Enter a parse tree produced by CSlangParser#operand4.
    def enterOperand4(self, ctx:CSlangParser.Operand4Context):
        pass

    # Exit a parse tree produced by CSlangParser#operand4.
    def exitOperand4(self, ctx:CSlangParser.Operand4Context):
        pass


    # Enter a parse tree produced by CSlangParser#operand5.
    def enterOperand5(self, ctx:CSlangParser.Operand5Context):
        pass

    # Exit a parse tree produced by CSlangParser#operand5.
    def exitOperand5(self, ctx:CSlangParser.Operand5Context):
        pass


    # Enter a parse tree produced by CSlangParser#listExps.
    def enterListExps(self, ctx:CSlangParser.ListExpsContext):
        pass

    # Exit a parse tree produced by CSlangParser#listExps.
    def exitListExps(self, ctx:CSlangParser.ListExpsContext):
        pass


    # Enter a parse tree produced by CSlangParser#listExpsNotNull.
    def enterListExpsNotNull(self, ctx:CSlangParser.ListExpsNotNullContext):
        pass

    # Exit a parse tree produced by CSlangParser#listExpsNotNull.
    def exitListExpsNotNull(self, ctx:CSlangParser.ListExpsNotNullContext):
        pass


    # Enter a parse tree produced by CSlangParser#listParams.
    def enterListParams(self, ctx:CSlangParser.ListParamsContext):
        pass

    # Exit a parse tree produced by CSlangParser#listParams.
    def exitListParams(self, ctx:CSlangParser.ListParamsContext):
        pass


    # Enter a parse tree produced by CSlangParser#indexOperator.
    def enterIndexOperator(self, ctx:CSlangParser.IndexOperatorContext):
        pass

    # Exit a parse tree produced by CSlangParser#indexOperator.
    def exitIndexOperator(self, ctx:CSlangParser.IndexOperatorContext):
        pass


    # Enter a parse tree produced by CSlangParser#memberAccess.
    def enterMemberAccess(self, ctx:CSlangParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by CSlangParser#memberAccess.
    def exitMemberAccess(self, ctx:CSlangParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by CSlangParser#staticMemberAccess.
    def enterStaticMemberAccess(self, ctx:CSlangParser.StaticMemberAccessContext):
        pass

    # Exit a parse tree produced by CSlangParser#staticMemberAccess.
    def exitStaticMemberAccess(self, ctx:CSlangParser.StaticMemberAccessContext):
        pass


    # Enter a parse tree produced by CSlangParser#instanceMethodInvocation.
    def enterInstanceMethodInvocation(self, ctx:CSlangParser.InstanceMethodInvocationContext):
        pass

    # Exit a parse tree produced by CSlangParser#instanceMethodInvocation.
    def exitInstanceMethodInvocation(self, ctx:CSlangParser.InstanceMethodInvocationContext):
        pass


    # Enter a parse tree produced by CSlangParser#staticMethodInvocation.
    def enterStaticMethodInvocation(self, ctx:CSlangParser.StaticMethodInvocationContext):
        pass

    # Exit a parse tree produced by CSlangParser#staticMethodInvocation.
    def exitStaticMethodInvocation(self, ctx:CSlangParser.StaticMethodInvocationContext):
        pass


    # Enter a parse tree produced by CSlangParser#objectCreation.
    def enterObjectCreation(self, ctx:CSlangParser.ObjectCreationContext):
        pass

    # Exit a parse tree produced by CSlangParser#objectCreation.
    def exitObjectCreation(self, ctx:CSlangParser.ObjectCreationContext):
        pass


    # Enter a parse tree produced by CSlangParser#listIds.
    def enterListIds(self, ctx:CSlangParser.ListIdsContext):
        pass

    # Exit a parse tree produced by CSlangParser#listIds.
    def exitListIds(self, ctx:CSlangParser.ListIdsContext):
        pass


    # Enter a parse tree produced by CSlangParser#listMixedIds.
    def enterListMixedIds(self, ctx:CSlangParser.ListMixedIdsContext):
        pass

    # Exit a parse tree produced by CSlangParser#listMixedIds.
    def exitListMixedIds(self, ctx:CSlangParser.ListMixedIdsContext):
        pass


    # Enter a parse tree produced by CSlangParser#varDeclStmt.
    def enterVarDeclStmt(self, ctx:CSlangParser.VarDeclStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#varDeclStmt.
    def exitVarDeclStmt(self, ctx:CSlangParser.VarDeclStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#valDeclStmt.
    def enterValDeclStmt(self, ctx:CSlangParser.ValDeclStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#valDeclStmt.
    def exitValDeclStmt(self, ctx:CSlangParser.ValDeclStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#declareWithAssign.
    def enterDeclareWithAssign(self, ctx:CSlangParser.DeclareWithAssignContext):
        pass

    # Exit a parse tree produced by CSlangParser#declareWithAssign.
    def exitDeclareWithAssign(self, ctx:CSlangParser.DeclareWithAssignContext):
        pass


    # Enter a parse tree produced by CSlangParser#declareWithoutAssign.
    def enterDeclareWithoutAssign(self, ctx:CSlangParser.DeclareWithoutAssignContext):
        pass

    # Exit a parse tree produced by CSlangParser#declareWithoutAssign.
    def exitDeclareWithoutAssign(self, ctx:CSlangParser.DeclareWithoutAssignContext):
        pass


    # Enter a parse tree produced by CSlangParser#assignStmt.
    def enterAssignStmt(self, ctx:CSlangParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#assignStmt.
    def exitAssignStmt(self, ctx:CSlangParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#assignStmtSemi.
    def enterAssignStmtSemi(self, ctx:CSlangParser.AssignStmtSemiContext):
        pass

    # Exit a parse tree produced by CSlangParser#assignStmtSemi.
    def exitAssignStmtSemi(self, ctx:CSlangParser.AssignStmtSemiContext):
        pass


    # Enter a parse tree produced by CSlangParser#ifStmt.
    def enterIfStmt(self, ctx:CSlangParser.IfStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#ifStmt.
    def exitIfStmt(self, ctx:CSlangParser.IfStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#preStmt.
    def enterPreStmt(self, ctx:CSlangParser.PreStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#preStmt.
    def exitPreStmt(self, ctx:CSlangParser.PreStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#elseStmt.
    def enterElseStmt(self, ctx:CSlangParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#elseStmt.
    def exitElseStmt(self, ctx:CSlangParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#forStmt.
    def enterForStmt(self, ctx:CSlangParser.ForStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#forStmt.
    def exitForStmt(self, ctx:CSlangParser.ForStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#breakStmt.
    def enterBreakStmt(self, ctx:CSlangParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#breakStmt.
    def exitBreakStmt(self, ctx:CSlangParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#continueStmt.
    def enterContinueStmt(self, ctx:CSlangParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#continueStmt.
    def exitContinueStmt(self, ctx:CSlangParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#returnStmt.
    def enterReturnStmt(self, ctx:CSlangParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#returnStmt.
    def exitReturnStmt(self, ctx:CSlangParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#methodInvocationStmt.
    def enterMethodInvocationStmt(self, ctx:CSlangParser.MethodInvocationStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#methodInvocationStmt.
    def exitMethodInvocationStmt(self, ctx:CSlangParser.MethodInvocationStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#blockStmt.
    def enterBlockStmt(self, ctx:CSlangParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#blockStmt.
    def exitBlockStmt(self, ctx:CSlangParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by CSlangParser#stmts.
    def enterStmts(self, ctx:CSlangParser.StmtsContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmts.
    def exitStmts(self, ctx:CSlangParser.StmtsContext):
        pass


    # Enter a parse tree produced by CSlangParser#stmt.
    def enterStmt(self, ctx:CSlangParser.StmtContext):
        pass

    # Exit a parse tree produced by CSlangParser#stmt.
    def exitStmt(self, ctx:CSlangParser.StmtContext):
        pass



del CSlangParser