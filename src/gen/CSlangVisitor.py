# Generated from D:/Bai tap/HL231/PPL/assignment3-initial/src/main/CSlang/parser/CSlang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CSlangParser import CSlangParser
else:
    from CSlangParser import CSlangParser

# This class defines a complete generic visitor for a parse tree produced by CSlangParser.

class CSlangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CSlangParser#program.
    def visitProgram(self, ctx:CSlangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classDecl.
    def visitClassDecl(self, ctx:CSlangParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#constructorDecl.
    def visitConstructorDecl(self, ctx:CSlangParser.ConstructorDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classStmtsNullable.
    def visitClassStmtsNullable(self, ctx:CSlangParser.ClassStmtsNullableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classStmt.
    def visitClassStmt(self, ctx:CSlangParser.ClassStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#attributeStmt.
    def visitAttributeStmt(self, ctx:CSlangParser.AttributeStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#singleDeclParam.
    def visitSingleDeclParam(self, ctx:CSlangParser.SingleDeclParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#declParams.
    def visitDeclParams(self, ctx:CSlangParser.DeclParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#listDeclParams.
    def visitListDeclParams(self, ctx:CSlangParser.ListDeclParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#methodDecl.
    def visitMethodDecl(self, ctx:CSlangParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#idLit.
    def visitIdLit(self, ctx:CSlangParser.IdLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#staticId.
    def visitStaticId(self, ctx:CSlangParser.StaticIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#mixedId.
    def visitMixedId(self, ctx:CSlangParser.MixedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#literal.
    def visitLiteral(self, ctx:CSlangParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#variableLit.
    def visitVariableLit(self, ctx:CSlangParser.VariableLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#indexedArrayLit.
    def visitIndexedArrayLit(self, ctx:CSlangParser.IndexedArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#nullLit.
    def visitNullLit(self, ctx:CSlangParser.NullLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#selfLit.
    def visitSelfLit(self, ctx:CSlangParser.SelfLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#booleanLit.
    def visitBooleanLit(self, ctx:CSlangParser.BooleanLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#primitiveType.
    def visitPrimitiveType(self, ctx:CSlangParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#classType.
    def visitClassType(self, ctx:CSlangParser.ClassTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#varType.
    def visitVarType(self, ctx:CSlangParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#arrayType.
    def visitArrayType(self, ctx:CSlangParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp.
    def visitExp(self, ctx:CSlangParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp1.
    def visitExp1(self, ctx:CSlangParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp2.
    def visitExp2(self, ctx:CSlangParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp3.
    def visitExp3(self, ctx:CSlangParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp4.
    def visitExp4(self, ctx:CSlangParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#exp5.
    def visitExp5(self, ctx:CSlangParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operand.
    def visitOperand(self, ctx:CSlangParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operand1.
    def visitOperand1(self, ctx:CSlangParser.Operand1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operand2.
    def visitOperand2(self, ctx:CSlangParser.Operand2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operand3.
    def visitOperand3(self, ctx:CSlangParser.Operand3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operand4.
    def visitOperand4(self, ctx:CSlangParser.Operand4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#operand5.
    def visitOperand5(self, ctx:CSlangParser.Operand5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#listExps.
    def visitListExps(self, ctx:CSlangParser.ListExpsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#listExpsNotNull.
    def visitListExpsNotNull(self, ctx:CSlangParser.ListExpsNotNullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#listParams.
    def visitListParams(self, ctx:CSlangParser.ListParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#indexOperator.
    def visitIndexOperator(self, ctx:CSlangParser.IndexOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#memberAccess.
    def visitMemberAccess(self, ctx:CSlangParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#staticMemberAccess.
    def visitStaticMemberAccess(self, ctx:CSlangParser.StaticMemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#instanceMethodInvocation.
    def visitInstanceMethodInvocation(self, ctx:CSlangParser.InstanceMethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#staticMethodInvocation.
    def visitStaticMethodInvocation(self, ctx:CSlangParser.StaticMethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#objectCreation.
    def visitObjectCreation(self, ctx:CSlangParser.ObjectCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#listIds.
    def visitListIds(self, ctx:CSlangParser.ListIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#listMixedIds.
    def visitListMixedIds(self, ctx:CSlangParser.ListMixedIdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#varDeclStmt.
    def visitVarDeclStmt(self, ctx:CSlangParser.VarDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#valDeclStmt.
    def visitValDeclStmt(self, ctx:CSlangParser.ValDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#declareWithAssign.
    def visitDeclareWithAssign(self, ctx:CSlangParser.DeclareWithAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#declareWithoutAssign.
    def visitDeclareWithoutAssign(self, ctx:CSlangParser.DeclareWithoutAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assignStmt.
    def visitAssignStmt(self, ctx:CSlangParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#assignStmtSemi.
    def visitAssignStmtSemi(self, ctx:CSlangParser.AssignStmtSemiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#ifStmt.
    def visitIfStmt(self, ctx:CSlangParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#preStmt.
    def visitPreStmt(self, ctx:CSlangParser.PreStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#elseStmt.
    def visitElseStmt(self, ctx:CSlangParser.ElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#forStmt.
    def visitForStmt(self, ctx:CSlangParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#breakStmt.
    def visitBreakStmt(self, ctx:CSlangParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#continueStmt.
    def visitContinueStmt(self, ctx:CSlangParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#returnStmt.
    def visitReturnStmt(self, ctx:CSlangParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#methodInvocationStmt.
    def visitMethodInvocationStmt(self, ctx:CSlangParser.MethodInvocationStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#blockStmt.
    def visitBlockStmt(self, ctx:CSlangParser.BlockStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmts.
    def visitStmts(self, ctx:CSlangParser.StmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CSlangParser#stmt.
    def visitStmt(self, ctx:CSlangParser.StmtContext):
        return self.visitChildren(ctx)



del CSlangParser