import unittest
from TestUtils import TestAST
# from AST import *
from main.CSlang.utils.AST import *



class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_class_with_one_decl_program(self):
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,301))

    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_class_with_one_decls(self):
        input = """class main {
               var b,c,d:int;
           }"""
        expect = str(Program([ClassDecl(Id("main"), [AttributeDecl(VarDecl(Id("b"), IntType())),AttributeDecl(VarDecl(Id("c"), IntType())),AttributeDecl(VarDecl(Id("d"), IntType()))])]))
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_4(self):
        input = """class main {
               var b,c,d:int = 1,2,3;
           }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("b"),IntType(),IntLiteral(1))),AttributeDecl(VarDecl(Id("c"),IntType(),IntLiteral(2))),AttributeDecl(VarDecl(Id("d"),IntType(),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_5(self):
        input = """class main {
            func a(b,c:float, d: int):int{}
        }"""
        expect = """Program([ClassDecl(Id(main),[MethodDecl(Id(a),[Param(Id(b),FloatType),Param(Id(c),FloatType),Param(Id(d),IntType)],IntType,Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,305))

    def test_6(self):
        input = """class object<-main{ const x, y, z: int = 1, 2, 3;var a, b: float;}"""
        expect = "Program([ClassDecl(Id(main),Id(object),[AttributeDecl(ConstDecl(Id(x),IntType,IntLit(1))),AttributeDecl(ConstDecl(Id(y),IntType,IntLit(2))),AttributeDecl(ConstDecl(Id(z),IntType,IntLit(3))),AttributeDecl(VarDecl(Id(a),FloatType)),AttributeDecl(VarDecl(Id(b),FloatType))])])"
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_7(self):
        input = """class main{ func a(): void {}}"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(a),[],VoidType,Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_8(self):
        input="""class main{
        func foo  (a: int, b: float):void {}
        
        func @main():void{
             io.printInt(4);
        }}"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(foo),[Param(Id(a),IntType),Param(Id(b),FloatType)],VoidType,Block([])),MethodDecl(Id(@main),[],VoidType,Block([Call(Id(io),Id(printInt),[IntLit(4)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_9(self):
        input = """class main {}class main2 {}"""
        expect = str(Program([ClassDecl(Id("main"),[]),ClassDecl(Id("main2"),[])]))
        self.assertTrue(TestAST.test(input,expect,309))

    def test_10(self):
        input = """class main {
            func constructor(){}
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(constructor),[],VoidType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,310))

    def test_11(self):
        input = """class main {
            func constructor(){}
            func method(): int{}
            const a: int;
            var b,c: int;
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(constructor),[],VoidType,Block([])),MethodDecl(Id(method),[],IntType,Block([])),AttributeDecl(ConstDecl(Id(a),IntType,None)),AttributeDecl(VarDecl(Id(b),IntType)),AttributeDecl(VarDecl(Id(c),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,311))

    def test_12(self):
        input = """class main {
            func constructor(){}
            func method(): int{}
            const a: int;
            var b: int;
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(constructor),[],VoidType,Block([])),MethodDecl(Id(method),[],IntType,Block([])),AttributeDecl(ConstDecl(Id(a),IntType,None)),AttributeDecl(VarDecl(Id(b),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,312))

    def test_13(self):
        input = """class main {
            func constructor(){}
            func method(): int{}
            const a,c: int;
            var b: int;
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(constructor),[],VoidType,Block([])),MethodDecl(Id(method),[],IntType,Block([])),AttributeDecl(ConstDecl(Id(a),IntType,None)),AttributeDecl(ConstDecl(Id(c),IntType,None)),AttributeDecl(VarDecl(Id(b),IntType))])])"
        self.assertTrue(TestAST.test(input,expect,313))

    def test_14(self):
        input = """class main {
            func method(a: int, b,c: float, c: float): int{}
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[Param(Id(a),IntType),Param(Id(b),FloatType),Param(Id(c),FloatType),Param(Id(c),FloatType)],IntType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,314))

    def test_15(self):
        input = """class main {
            func method(a,b: int): int{}
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[Param(Id(a),IntType),Param(Id(b),IntType)],IntType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,315))

    def test_16(self):
        input = """class main {
            func method(): int{}
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,316))


    def test_17(self):
        input = """class main {
            func @method(): int{}
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([]))])])"
        self.assertTrue(TestAST.test(input,expect,317))

    def test_18(self):
        input = """class main {
            func @method(): int{
                var a: int;
                a := 1 + 2 + 3;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input,expect,318))

    def test_19(self):
        input = """class main {
            func @method(): int{
                var a,b,c: int;
                a := 1.0 + 2.0 + 3.0;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,FloatLit(1.0),FloatLit(2.0)),FloatLit(3.0)))]))])])"
        self.assertTrue(TestAST.test(input,expect,319))

    def test_20(self):
        input = """class main {
            func @method(): int{
                var a: int;
                a := true;
                a := false;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),BooleanLit(True)),AssignStmt(Id(a),BooleanLit(False))]))])])"
        self.assertTrue(TestAST.test(input,expect,320))

    def test_21(self):
        input = """class main {
            func @method(): int{
                var a: string;
                a := "String";
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([VarDecl(Id(a),StringType),AssignStmt(Id(a),StringLit(String))]))])])"
        self.assertTrue(TestAST.test(input,expect,321))

    def test_22(self):
        input = """class main {
            func @method(): int{
                var a: [4]int;
                a := [1,2,3,4];
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([VarDecl(Id(a),ArrayType(4,IntType)),AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])]))])])"
        self.assertTrue(TestAST.test(input,expect,322))

    def test_23(self):
        input = """class main {
            func @method(): int{
                var a: int;
                a := [1,2,3,4];
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])]))])])"
        self.assertTrue(TestAST.test(input,expect,323))

    def test_24(self):
        input = """class main {
            func @method(): int{
                var a: int;
                a := self;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),Self())]))])])"
        self.assertTrue(TestAST.test(input,expect,324))

    def test_25(self):
        input = """class main {
            func @method(): int{
                var a: int;
                a := null;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(@method),[],IntType,Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),NullLiteral())]))])])"
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_26(self):
        input = """class main {
            func method(): int{
                var a: int;
                a.member := 1;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(a),IntType),AssignStmt(FieldAccess(Id(a),Id(member)),IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_27(self):
        input = """class main {
            var @a: int;
            func method(): int{
                @a := 1;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(VarDecl(Id(@a),IntType)),MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(@a),IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_28(self):
        input = """class main {
            func method(): int{
                var a: int;
                var b: float;
                var c: string;
                var d: bool;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(a),IntType),VarDecl(Id(b),FloatType),VarDecl(Id(c),StringType),VarDecl(Id(d),BoolType)]))])])"
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_29(self):
        input = """class main {
            func method(): int{
                var a: [4]float;
                var a: [4]string;
                var a: [4]bool;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(a),ArrayType(4,FloatType)),VarDecl(Id(a),ArrayType(4,StringType)),VarDecl(Id(a),ArrayType(4,BoolType))]))])])"
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_30(self):
        input = """class main {
            func method(): int{
                var a: [4]int;
                var b: Class1;
                var c: void;
            }
        } class Class1{
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(a),ArrayType(4,IntType)),VarDecl(Id(b),Id(Class1)),VarDecl(Id(c),VoidType)]))]),ClassDecl(Id(Class1),[])])"
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_31(self):
        input = """class main {
            func method(): int{
                var a,b: int = 1, 2;
            }
        } class Class1{
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),IntType,IntLit(2))]))]),ClassDecl(Id(Class1),[])])"
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_32(self):
        input = """class main {
            func method(): int{
                var a,b: int = 1, 2;
                var c, d, e: float = 1.2, 2.3, 3.4233;
                var f: void = null;
            }
        } class Class1{
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),IntType,IntLit(2)),VarDecl(Id(c),FloatType,FloatLit(1.2)),VarDecl(Id(d),FloatType,FloatLit(2.3)),VarDecl(Id(e),FloatType,FloatLit(3.4233)),VarDecl(Id(f),VoidType,NullLiteral())]))]),ClassDecl(Id(Class1),[])])"
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_33(self):
        input = """class main {
            func method(): int{
                a := "122" ^ "123";
                b := "831923" ^ "123" ^ "123";
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(^,StringLit(122),StringLit(123))),AssignStmt(Id(b),BinaryOp(^,BinaryOp(^,StringLit(831923),StringLit(123)),StringLit(123)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_34(self):
        input = """class main {
            func method(): int{
                a := "122" == "123";
                b := "831923" != "123" == "123";
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(==,StringLit(122),StringLit(123))),AssignStmt(Id(b),BinaryOp(==,BinaryOp(!=,StringLit(831923),StringLit(123)),StringLit(123)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_35(self):
        input = """class main {
            func method(): int{
                a := "122" || "123";
                b := "831923" || "123" || "123";
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(||,StringLit(122),StringLit(123))),AssignStmt(Id(b),BinaryOp(||,BinaryOp(||,StringLit(831923),StringLit(123)),StringLit(123)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_36(self):
        input = """class main {
            func method(): int{
                a := "122" && "123";
                b := "831923" && "123" && "123";
                b := "831923" && "123" && "123" ^ "123";
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(&&,StringLit(122),StringLit(123))),AssignStmt(Id(b),BinaryOp(&&,BinaryOp(&&,StringLit(831923),StringLit(123)),StringLit(123))),AssignStmt(Id(b),BinaryOp(^,BinaryOp(&&,BinaryOp(&&,StringLit(831923),StringLit(123)),StringLit(123)),StringLit(123)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_37(self):
        input = """class main {
            func method(): int{
                a := 1 + 2 * 3 / 4 + 5;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4))),IntLit(5)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_38(self):
        input = """class main {
            func method(): int{
                a := 1 * 2 * 3 / 4 * 5;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(*,BinaryOp(/,BinaryOp(*,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_39(self):
        input = """class main {
            func method(): int{
                a := 1 * 2 % 3 / 4 * 5;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(*,BinaryOp(/,BinaryOp(%,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),IntLit(4)),IntLit(5)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_40(self):
        input = """class main {
            func method(): int{
                a := !n || !!b  ||  3 / 4 * 5;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(||,BinaryOp(||,UnaryOp(!,Id(n)),UnaryOp(!,UnaryOp(!,Id(b)))),BinaryOp(*,BinaryOp(/,IntLit(3),IntLit(4)),IntLit(5))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_41(self):
        input = """class main {
            func method(): int{
                a := -5 * -2 + --2;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(*,UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(2))),UnaryOp(-,UnaryOp(-,IntLit(2)))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_42(self):
        input = """class main {
            func method(): int{
                a := a[5];
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),ArrayCell(Id(a),IntLit(5)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_43(self):
        input = """class main {
            func method(): int{
                a := a[5][1];
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),ArrayCell(ArrayCell(Id(a),IntLit(5)),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_44(self):
        input = """class main {
            func method(): int{
                a := a[5 || 1][1+self.a()];
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),ArrayCell(ArrayCell(Id(a),BinaryOp(||,IntLit(5),IntLit(1))),BinaryOp(+,IntLit(1),CallExpr(Self(),Id(a),[]))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_45(self):
        input = """class main {
            func method(): int{
                a := a.b + a.b();
            }
        }"""
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_45(self):
        input = """class main {
            func method(): int{
                a := a.b + a.b();
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(+,FieldAccess(Id(a),Id(b)),CallExpr(Id(a),Id(b),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_46(self):
        input = """class main {
            func method(): int{
                a := @a.b + @b() + @a.b();
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,FieldAccess(Id(@a),Id(b)),CallExpr(Id(@b),[])),CallExpr(Id(@a),Id(b),[])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_47(self):
        input = """class main {
            func method(): int{
                a[3+x.foo(2)] := a[b[2]] +3;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(ArrayCell(Id(a),BinaryOp(+,IntLit(3),CallExpr(Id(x),Id(foo),[IntLit(2)]))),BinaryOp(+,ArrayCell(Id(a),ArrayCell(Id(b),IntLit(2))),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_48(self):
        input = """class main {
            func method(): int{
                a := new Class1();
                a := new Class1(new Class2());
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),NewExpr(Id(Class1),[])),AssignStmt(Id(a),NewExpr(Id(Class1),[NewExpr(Id(Class2),[])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_49(self):
        input = """class main {
            func method(): int{
                a := 1 + 2 * ((new Pb()) + 4);
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),BinaryOp(+,NewExpr(Id(Pb),[]),IntLit(4)))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_50(self):
        input = """class main {
            func method(): int{
                a := a.b.c.d;
                a := a.b().c.d();
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d))),AssignStmt(Id(a),CallExpr(FieldAccess(CallExpr(Id(a),Id(b),[]),Id(c)),Id(d),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_51(self):
        input = """class main {
            func method(): int{
                a := @a.d;
                a := @a.d();
                a := @a.d(1+1);
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([AssignStmt(Id(a),FieldAccess(Id(@a),Id(d))),AssignStmt(Id(a),CallExpr(Id(@a),Id(d),[])),AssignStmt(Id(a),CallExpr(Id(@a),Id(d),[BinaryOp(+,IntLit(1),IntLit(1))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_52(self):
        input = """class main {
            func method(): int{
                a.@d(1,2,3);
                @d(1,2,3);
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([Call(Id(a),Id(@d),[IntLit(1),IntLit(2),IntLit(3)]),Call(Id(@d),[IntLit(1),IntLit(2),IntLit(3)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_53(self):
        input = """class main {
            func method(): int{
                a.d(1,2,3);
                a.d(new Class(1,2,3),4,5);
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([Call(Id(a),Id(d),[IntLit(1),IntLit(2),IntLit(3)]),Call(Id(a),Id(d),[NewExpr(Id(Class),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(4),IntLit(5)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_54(self):
        input = """class main {
            func method(): int{
                a.d(1,2,3);
                a.d(new Class(1,2,3),4,5);
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([Call(Id(a),Id(d),[IntLit(1),IntLit(2),IntLit(3)]),Call(Id(a),Id(d),[NewExpr(Id(Class),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(4),IntLit(5)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_55(self):
        input = """class main {
            func method(): int{
                var a,b,c: int = 2+3, 4,5;
                const d,e,f: float = 3.0, 4.0, 5.0;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(a),IntType,BinaryOp(+,IntLit(2),IntLit(3))),VarDecl(Id(b),IntType,IntLit(4)),VarDecl(Id(c),IntType,IntLit(5)),ConstDecl(Id(d),FloatType,FloatLit(3.0)),ConstDecl(Id(e),FloatType,FloatLit(4.0)),ConstDecl(Id(f),FloatType,FloatLit(5.0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_56(self):
        input = """class main {
            func method(): int{
                var @a,b,@c: int = 2+3, 4,5;
                const d,@e,@f: float = 3.0, 4.0, 5.0;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(@a),IntType,BinaryOp(+,IntLit(2),IntLit(3))),VarDecl(Id(b),IntType,IntLit(4)),VarDecl(Id(@c),IntType,IntLit(5)),ConstDecl(Id(d),FloatType,FloatLit(3.0)),ConstDecl(Id(@e),FloatType,FloatLit(4.0)),ConstDecl(Id(@f),FloatType,FloatLit(5.0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_57(self):
        input = """class main {
            func method(): int{
                var r, s: tnt;
                r := 2.0;
                var a, b: [5]int;
                s := r * r * self.myPI;
                a[0] := s;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(r),Id(tnt)),VarDecl(Id(s),Id(tnt)),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),IntLit(0)),Id(s))]))])])"
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_58(self):
        input = """class main {
            func method(): int{
                break;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([Break]))])])"
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_59(self):
        input = """class main {
            func method(): int{
                continue;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([Continue]))])])"
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_60(self):
        input = """class main {
            func method(): int{
                return;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_61(self):
        input = """class main {
            func method(): int{
                return a;
                return 1+2+3;
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([Return(Id(a)),Return(BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_62(self):
        input = """class main {
            func method(): int{
                return new Class();
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([Return(NewExpr(Id(Class),[]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_63(self):
        input = """class main {
            func method(): int{
                var i: int;
                if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(i),IntType),If(Block([AssignStmt(Id(i),IntLit(0))]),BinaryOp(>,Id(j),Id(i)),Block([AssignStmt(Id(j),BinaryOp(-,Id(j),IntLit(1)))]),Block([AssignStmt(Id(j),BinaryOp(+,Id(j),IntLit(1)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_64(self):
        input = """class main {
            func method(): int{
                var i: int;
                if {} j > i {} else {}
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([VarDecl(Id(i),IntType),If(Block([]),BinaryOp(>,Id(j),Id(i)),Block([]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 364))


    def test_65(self):
        input = """class main {
            func method(): int{
                if j > i {} else {}
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([If(BinaryOp(>,Id(j),Id(i)),Block([]),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 365))


    def test_66(self):
        input = """class main {
            func method(): int{
                if j > i {i:=i+1;}
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([If(BinaryOp(>,Id(j),Id(i)),Block([AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 366))


    def test_67(self):
        input = """class main {
            func method(): int{
                if j > i {}
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([If(BinaryOp(>,Id(j),Id(i)),Block([]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 367))


    def test_68(self):
        input = """class main {
            func method(): int{
                for i := 0; i < 10; i := i + 1 {
                    io.@writeInt(i);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@writeInt),[Id(i)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 368))


    def test_69(self):
        input = """class main {
            func method(): int{
                for i := 0; i < 10; i := i + 1 {
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(main),[MethodDecl(Id(method),[],IntType,Block([For(AssignStmt(Id(i),IntLit(0)),BinaryOp(<,Id(i),IntLit(10)),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 369))


    def test_70(self):
        input = """class GuiComponents <- MenuItem{
            func draw(g2d: Graphic2D): void{
                g2d.setFont(font);
                g2d.setColor(fontColor);
                g2d.drawString(LABEL, bounds.x + 5, bounds.y + 15);
            }
        }"""
        expect = "Program([ClassDecl(Id(MenuItem),Id(GuiComponents),[MethodDecl(Id(draw),[Param(Id(g2d),Id(Graphic2D))],VoidType,Block([Call(Id(g2d),Id(setFont),[Id(font)]),Call(Id(g2d),Id(setColor),[Id(fontColor)]),Call(Id(g2d),Id(drawString),[Id(LABEL),BinaryOp(+,FieldAccess(Id(bounds),Id(x)),IntLit(5)),BinaryOp(+,FieldAccess(Id(bounds),Id(y)),IntLit(15))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 370))


    def test_71(self):
        input = """class Program{
                func update(gametime: GameTime): void{
                    if bounds.intersects(){
                        fontColor := hoverColor;
                        Rectangle.@onHover();
                        if(Mouse.buttonDownOnce(MouseKeys.BUTTON_1)){
                            Test.onClick();
                        }
                    } else {
                         fontColor := Color.WHITE;
                    }
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(update),[Param(Id(gametime),Id(GameTime))],VoidType,Block([If(CallExpr(Id(bounds),Id(intersects),[]),Block([AssignStmt(Id(fontColor),Id(hoverColor)),Call(Id(Rectangle),Id(@onHover),[]),If(CallExpr(Id(Mouse),Id(buttonDownOnce),[FieldAccess(Id(MouseKeys),Id(BUTTON_1))]),Block([Call(Id(Test),Id(onClick),[])]))]),Block([AssignStmt(Id(fontColor),FieldAccess(Id(Color),Id(WHITE)))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 371))


    def test_72(self):
        input = """class ActionListener <- FlappyBird {
                const @FPS, @WIDTH, @HEIGHT: int = 60, 640, 480;
                var bird: Bird;
                var frame: JFrame;
                var jpanel: JPanel;
                const rects: [5]string;
                const time, scroll: int;
                const paused: bool;
            }"""
        expect = "Program([ClassDecl(Id(FlappyBird),Id(ActionListener),[AttributeDecl(ConstDecl(Id(@FPS),IntType,IntLit(60))),AttributeDecl(ConstDecl(Id(@WIDTH),IntType,IntLit(640))),AttributeDecl(ConstDecl(Id(@HEIGHT),IntType,IntLit(480))),AttributeDecl(VarDecl(Id(bird),Id(Bird))),AttributeDecl(VarDecl(Id(frame),Id(JFrame))),AttributeDecl(VarDecl(Id(jpanel),Id(JPanel))),AttributeDecl(ConstDecl(Id(rects),ArrayType(5,StringType),None)),AttributeDecl(ConstDecl(Id(time),IntType,None)),AttributeDecl(ConstDecl(Id(scroll),IntType,None)),AttributeDecl(ConstDecl(Id(paused),BoolType,None))])])"
        self.assertTrue(TestAST.test(input, expect, 372))


    def test_73(self):
        input = """class Test_Mix{
                func actionPerformed(e: ActionEvent): void{
                    panel.repaint();
                    if(!paused){
                        bird.physics();
                        if(scoll % 90 == 0){
                            rects.add(r);
                            rects.add(r2);
                        }
                        if(bird.y > HEIGHT || (bird.y + bird.RAD < 0)) {
                            game := false;
                        }
                        if((x+y > height) || (x - y >= 0)){}
                    }
                }
            }"""
        expect = "Program([ClassDecl(Id(Test_Mix),[MethodDecl(Id(actionPerformed),[Param(Id(e),Id(ActionEvent))],VoidType,Block([Call(Id(panel),Id(repaint),[]),If(UnaryOp(!,Id(paused)),Block([Call(Id(bird),Id(physics),[]),If(BinaryOp(==,BinaryOp(%,Id(scoll),IntLit(90)),IntLit(0)),Block([Call(Id(rects),Id(add),[Id(r)]),Call(Id(rects),Id(add),[Id(r2)])])),If(BinaryOp(>,FieldAccess(Id(bird),Id(y)),BinaryOp(||,Id(HEIGHT),BinaryOp(<,BinaryOp(+,FieldAccess(Id(bird),Id(y)),FieldAccess(Id(bird),Id(RAD))),IntLit(0)))),Block([AssignStmt(Id(game),BooleanLit(False))])),If(BinaryOp(||,BinaryOp(>,BinaryOp(+,Id(x),Id(y)),Id(height)),BinaryOp(>=,BinaryOp(-,Id(x),Id(y)),IntLit(0))),Block([]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 373))


    def test_74(self):
        input = """class Test_Array{
                const array: [5]int = [1,2,3,4];
                const array: [5]int = [1,2,3,4];
        }"""
        expect = "Program([ClassDecl(Id(Test_Array),[AttributeDecl(ConstDecl(Id(array),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AttributeDecl(ConstDecl(Id(array),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]))])])"
        self.assertTrue(TestAST.test(input, expect, 374))


    def test_75(self):
        input = """class Calculator{
            func constructor() {
                window := new JFrame("Calculator");
                window.window.setSize(WINDOW_WIDTH, WINDOW_HEIGHT);
                window.window.setLocationRelativeTo(null);
                comboTheme :=  new text("Simple", "Colored", "DarkTheme", 230, 30, "Theme", themeSwitchEventConsumer);
                comboCalcType :=  new text("Standard", "Scientific", 20, 30, "Calculator type", calcTypeSwitchEventConsumer);
                var x: [1]int = [MARGIN_X, MARGIN_X + 90, 200, 290, 380];
                var y: [2]int = [MARGIN_Y, MARGIN_Y + 100, MARGIN_Y + 180, MARGIN_Y + 260, MARGIN_Y + 340, MARGIN_Y + 420];
            }
        }"""
        expect = "Program([ClassDecl(Id(Calculator),[MethodDecl(Id(constructor),[],VoidType,Block([AssignStmt(Id(window),NewExpr(Id(JFrame),[StringLit(Calculator)])),Call(FieldAccess(Id(window),Id(window)),Id(setSize),[Id(WINDOW_WIDTH),Id(WINDOW_HEIGHT)]),Call(FieldAccess(Id(window),Id(window)),Id(setLocationRelativeTo),[NullLiteral()]),AssignStmt(Id(comboTheme),NewExpr(Id(text),[StringLit(Simple),StringLit(Colored),StringLit(DarkTheme),IntLit(230),IntLit(30),StringLit(Theme),Id(themeSwitchEventConsumer)])),AssignStmt(Id(comboCalcType),NewExpr(Id(text),[StringLit(Standard),StringLit(Scientific),IntLit(20),IntLit(30),StringLit(Calculator type),Id(calcTypeSwitchEventConsumer)])),VarDecl(Id(x),ArrayType(1,IntType),[Id(MARGIN_X),BinaryOp(+,Id(MARGIN_X),IntLit(90)),IntLit(200),IntLit(290),IntLit(380)]),VarDecl(Id(y),ArrayType(2,IntType),[Id(MARGIN_Y),BinaryOp(+,Id(MARGIN_Y),IntLit(100)),BinaryOp(+,Id(MARGIN_Y),IntLit(180)),BinaryOp(+,Id(MARGIN_Y),IntLit(260)),BinaryOp(+,Id(MARGIN_Y),IntLit(340)),BinaryOp(+,Id(MARGIN_Y),IntLit(420))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 375))


    def test_76(self):
        input = """class Program {
            func getTicket(type : Type): string{
                return "Premium";
            }
            func main(): void{
                if(x >= y){
                    var x: int = 10 + 20;
                    x := x + 3;
                }
                else {
                    self.getTicket(code);
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(getTicket),[Param(Id(type),Id(Type))],StringType,Block([Return(StringLit(Premium))])),MethodDecl(Id(main),[],VoidType,Block([If(BinaryOp(>=,Id(x),Id(y)),Block([VarDecl(Id(x),IntType,BinaryOp(+,IntLit(10),IntLit(20))),AssignStmt(Id(x),BinaryOp(+,Id(x),IntLit(3)))]),Block([Call(Self(),Id(getTicket),[Id(code)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 376))


    def test_77(self):
        input = """class Test_boolean {
            func foo(): void{
                if ( a == -1-(-1)){
                    if(that == false){}
                }
            }
        }"""
        expect = "Program([ClassDecl(Id(Test_boolean),[MethodDecl(Id(foo),[],VoidType,Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([If(BinaryOp(==,Id(that),BooleanLit(False)),Block([]))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 377))


    def test_78(self):
        input = """class Test_boolean{
            func hZA2(): void{
                _4J := _s_ <= ___KS__ >= uR;
            }
        }"""
        expect = "Program([ClassDecl(Id(Test_boolean),[MethodDecl(Id(hZA2),[],VoidType,Block([AssignStmt(Id(_4J),BinaryOp(>=,BinaryOp(<=,Id(_s_),Id(___KS__)),Id(uR)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 378))


    def test_79(self):
        input = """class Premium {
            func foo(): void{
                a := ("_p"^"__")^"IK_4";
                c := ("nL"=="_H")==true;
            } 
        }"""
        expect = "Program([ClassDecl(Id(Premium),[MethodDecl(Id(foo),[],VoidType,Block([AssignStmt(Id(a),BinaryOp(^,BinaryOp(^,StringLit(_p),StringLit(__)),StringLit(IK_4))),AssignStmt(Id(c),BinaryOp(==,BinaryOp(==,StringLit(nL),StringLit(_H)),BooleanLit(True)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 379))


    def test_80(self):
        input = """class Shape {
            func foo(): void{
                _IA.@GB:=7;
                M.@e();
                f6h.@c.@w:=5;
            } 
        }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),[],VoidType,Block([AssignStmt(FieldAccess(Id(_IA),Id(@GB)),IntLit(7)),Call(Id(M),Id(@e),[]),AssignStmt(FieldAccess(FieldAccess(Id(f6h),Id(@c)),Id(@w)),IntLit(5))]))])])"
        self.assertTrue(TestAST.test(input, expect, 380))


    def test_81(self):
        input = """class Test_boolean{
                func foo(): void{
                    F8_ := R3A == e_ == A_3;
                }
            }"""
        expect = "Program([ClassDecl(Id(Test_boolean),[MethodDecl(Id(foo),[],VoidType,Block([AssignStmt(Id(F8_),BinaryOp(==,BinaryOp(==,Id(R3A),Id(e_)),Id(A_3)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 381))


    def test_82(self):
        input = """class Program {
            func method():void {
                for r:=2;r<=100;r:=r+1 {
                r.x := r.x - 3;
                if r.x + r.width <= 0 {
                    toRemove.add(r);
                    a := "You lose!\\n" ^ "Your score was: " ^ time ^ ".";
                    JOptionPane.showMessageDialog(frame, a);
                }
                if r.contains(bird.x, bird.y){
                } 
            }
        }}"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(method),[],VoidType,Block([For(AssignStmt(Id(r),IntLit(2)),BinaryOp(<=,Id(r),IntLit(100)),AssignStmt(Id(r),BinaryOp(+,Id(r),IntLit(1))),Block([AssignStmt(FieldAccess(Id(r),Id(x)),BinaryOp(-,FieldAccess(Id(r),Id(x)),IntLit(3))),If(BinaryOp(<=,BinaryOp(+,FieldAccess(Id(r),Id(x)),FieldAccess(Id(r),Id(width))),IntLit(0)),Block([Call(Id(toRemove),Id(add),[Id(r)]),AssignStmt(Id(a),BinaryOp(^,BinaryOp(^,BinaryOp(^,StringLit(You lose!\\n),StringLit(Your score was: )),Id(time)),StringLit(.))),Call(Id(JOptionPane),Id(showMessageDialog),[Id(frame),Id(a)])])),If(CallExpr(Id(r),Id(contains),[FieldAccess(Id(bird),Id(x)),FieldAccess(Id(bird),Id(y))]),Block([]))])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 382))


    def test_83(self):
        input ="""class Program {
                func Program(): void{
                    a := -11111112 + 1222333455665;
                    b := 6 + -3 - -2 + -10 - -11111111111;
                } 
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Program),[],VoidType,Block([AssignStmt(Id(a),BinaryOp(+,UnaryOp(-,IntLit(11111112)),IntLit(1222333455665))),AssignStmt(Id(b),BinaryOp(-,BinaryOp(+,BinaryOp(-,BinaryOp(+,IntLit(6),UnaryOp(-,IntLit(3))),UnaryOp(-,IntLit(2))),UnaryOp(-,IntLit(10))),UnaryOp(-,IntLit(11111111111))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 383))


    def test_84(self):
        input ="""class Program {
              var x: int = 65;
              func @fact(n: int):int {
                if n == 0 {return 1;}
                else {return n * @fact(n - 1);}
        }}"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(VarDecl(Id(x),IntType,IntLit(65))),MethodDecl(Id(@fact),[Param(Id(n),IntType)],IntType,Block([If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(1))]),Block([Return(BinaryOp(*,Id(n),CallExpr(Id(@fact),[BinaryOp(-,Id(n),IntLit(1))])))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 384))


    def test_85(self):
        input = """class Premium {
                func doDrawing(g:Graphics ):void {
                    if (inGame) {
                        g.drawImage(apple, apple_x, apple_y, this);
                        for z:=10;z<=100;z:=z+3 {
                            if (z == 0) {
                                g.drawImage(head, x[z], y[z], this);
                            } else {
                                g.drawImage(ball, x[z], y[z], this);
                            }
                        }
                        Toolkit.getDefaultToolkit().sync();
                    } else {
                        name.gameOver(g);
                    }        
                }
            }"""
        expect = "Program([ClassDecl(Id(Premium),[MethodDecl(Id(doDrawing),[Param(Id(g),Id(Graphics))],VoidType,Block([If(Id(inGame),Block([Call(Id(g),Id(drawImage),[Id(apple),Id(apple_x),Id(apple_y),Id(this)]),For(AssignStmt(Id(z),IntLit(10)),BinaryOp(<=,Id(z),IntLit(100)),AssignStmt(Id(z),BinaryOp(+,Id(z),IntLit(3))),Block([If(BinaryOp(==,Id(z),IntLit(0)),Block([Call(Id(g),Id(drawImage),[Id(head),ArrayCell(Id(x),Id(z)),ArrayCell(Id(y),Id(z)),Id(this)])]),Block([Call(Id(g),Id(drawImage),[Id(ball),ArrayCell(Id(x),Id(z)),ArrayCell(Id(y),Id(z)),Id(this)])]))])]),Call(CallExpr(Id(Toolkit),Id(getDefaultToolkit),[]),Id(sync),[])]),Block([Call(Id(name),Id(gameOver),[Id(g)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 385))


    def test_86(self):
        input = """class _{
            const @_g28:[10]bool;
            var _,@_:[10]int;
            func constructor (b:s, T_f2:[10]int){}
        }"""
        expect = "Program([ClassDecl(Id(_),[AttributeDecl(ConstDecl(Id(@_g28),ArrayType(10,BoolType),None)),AttributeDecl(VarDecl(Id(_),ArrayType(10,IntType))),AttributeDecl(VarDecl(Id(@_),ArrayType(10,IntType))),MethodDecl(Id(constructor),[Param(Id(b),Id(s)),Param(Id(T_f2),ArrayType(10,IntType))],VoidType,Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 386))


    def test_87(self):
        input = """class Program {
            func foo(): void{
                for i:=(1---2+3333/4364563+1000000);i<=(3+4+5);i:=i+(16-14) {
                    System.printOut(i);
                }
            } 
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(foo),[],VoidType,Block([For(AssignStmt(Id(i),BinaryOp(+,BinaryOp(+,BinaryOp(-,IntLit(1),UnaryOp(-,UnaryOp(-,IntLit(2)))),BinaryOp(/,IntLit(3333),IntLit(4364563))),IntLit(1000000))),BinaryOp(<=,Id(i),BinaryOp(+,BinaryOp(+,IntLit(3),IntLit(4)),IntLit(5))),AssignStmt(Id(i),BinaryOp(+,Id(i),BinaryOp(-,IntLit(16),IntLit(14)))),Block([Call(Id(System),Id(printOut),[Id(i)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 387))


    def test_88(self):
        input = """class M {
            func VAU(): void{
                G5[G5[1]][G5][self.G5()] := 1;
            }
        }"""
        expect = "Program([ClassDecl(Id(M),[MethodDecl(Id(VAU),[],VoidType,Block([AssignStmt(ArrayCell(ArrayCell(ArrayCell(Id(G5),ArrayCell(Id(G5),IntLit(1))),Id(G5)),CallExpr(Self(),Id(G5),[])),IntLit(1))]))])])"
        self.assertTrue(TestAST.test(input, expect, 388))


    def test_89(self):
        input = """class Program {
            // something
            /* sjkljdkfljfkl
            // a = 5+x;
            */
        }"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input, expect, 389))


    def test_90(self):
        input = """class Program {
            const a: int = 1;
            func main(): void{
                var delta: int = @fact(3);
                delta.fact := 3 + x;
                delta.@fact := 3 + foo.x;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id(main),[],VoidType,Block([VarDecl(Id(delta),IntType,CallExpr(Id(@fact),[IntLit(3)])),AssignStmt(FieldAccess(Id(delta),Id(fact)),BinaryOp(+,IntLit(3),Id(x))),AssignStmt(FieldAccess(Id(delta),Id(@fact)),BinaryOp(+,IntLit(3),FieldAccess(Id(foo),Id(x))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 390))


    def test_91(self):
        input = """class Program{ 
                const a: int = new B(new A().@attr2).attr();
            }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(ConstDecl(Id(a),IntType,CallExpr(NewExpr(Id(B),[FieldAccess(NewExpr(Id(A),[]),Id(@attr2))]),Id(attr),[])))])])"
        self.assertTrue(TestAST.test(input, expect, 391))


    def test_92(self):
        input = """class Program{ 
                const a: int = new B(new A().@attr2(5, --2)).attr;
            }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(ConstDecl(Id(a),IntType,FieldAccess(NewExpr(Id(B),[CallExpr(NewExpr(Id(A),[]),Id(@attr2),[IntLit(5),UnaryOp(-,UnaryOp(-,IntLit(2)))])]),Id(attr))))])])"
        self.assertTrue(TestAST.test(input, expect, 392))


    def test_93(self):
        input = """class Program {
                func draw(g2d: Graphic2D): void{
                    g2d.setFont(font);
                    g2d.setColor(fontColor);
                    g2d.drawString(LABEL, bounds.x + 5, bounds.y + 15);
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(draw),[Param(Id(g2d),Id(Graphic2D))],VoidType,Block([Call(Id(g2d),Id(setFont),[Id(font)]),Call(Id(g2d),Id(setColor),[Id(fontColor)]),Call(Id(g2d),Id(drawString),[Id(LABEL),BinaryOp(+,FieldAccess(Id(bounds),Id(x)),IntLit(5)),BinaryOp(+,FieldAccess(Id(bounds),Id(y)),IntLit(15))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 393))


    def test_94(self):
        input = """class Program {
                func method(): void {
                    intext.setBackground(Color.WHITE);
                    intext.setFont(new Font("Comic Sans MS", Font.PLAIN, 33));
                    window.add(intext);
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(method),[],VoidType,Block([Call(Id(intext),Id(setBackground),[FieldAccess(Id(Color),Id(WHITE))]),Call(Id(intext),Id(setFont),[NewExpr(Id(Font),[StringLit(Comic Sans MS),FieldAccess(Id(Font),Id(PLAIN)),IntLit(33)])]),Call(Id(window),Id(add),[Id(intext)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 394))


    def test_95(self):
        input = """class Program {
                func method(): void {
                    intext := new JTextField("0");
                    intext.setBounds(x[0], y[0], 350, 70);
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(method),[],VoidType,Block([AssignStmt(Id(intext),NewExpr(Id(JTextField),[StringLit(0)])),Call(Id(intext),Id(setBounds),[ArrayCell(Id(x),IntLit(0)),ArrayCell(Id(y),IntLit(0)),IntLit(350),IntLit(70)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 395))


    def test_96(self):
        input = """class S{
                const r: Rectangle = new Rectangle(WIDTH, 0, GamePanel.PIPE_W, (Math.random()*HEIGHT)/5 + 0.2 * HEIGHT);
                var h2: int = (Math.random()*HEIGHT)/5 + 0.2 * HEIGHT;
                var r2: Rectangle = new Rectangle(WIDTH, HEIGHT - h2, GamePanel.PIPE_W, h2);
            }"""
        expect = "Program([ClassDecl(Id(S),[AttributeDecl(ConstDecl(Id(r),Id(Rectangle),NewExpr(Id(Rectangle),[Id(WIDTH),IntLit(0),FieldAccess(Id(GamePanel),Id(PIPE_W)),BinaryOp(+,BinaryOp(/,BinaryOp(*,CallExpr(Id(Math),Id(random),[]),Id(HEIGHT)),IntLit(5)),BinaryOp(*,FloatLit(0.2),Id(HEIGHT)))]))),AttributeDecl(VarDecl(Id(h2),IntType,BinaryOp(+,BinaryOp(/,BinaryOp(*,CallExpr(Id(Math),Id(random),[]),Id(HEIGHT)),IntLit(5)),BinaryOp(*,FloatLit(0.2),Id(HEIGHT))))),AttributeDecl(VarDecl(Id(r2),Id(Rectangle),NewExpr(Id(Rectangle),[Id(WIDTH),BinaryOp(-,Id(HEIGHT),Id(h2)),FieldAccess(Id(GamePanel),Id(PIPE_W)),Id(h2)])))])])"
        self.assertTrue(TestAST.test(input, expect, 396))


    def test_97(self):
        input = """class Program {
                func main(): void{
                    return new VAU(new VAU(new VAU()), 1+2, C.@VAU);
                }
            }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),[],VoidType,Block([Return(NewExpr(Id(VAU),[NewExpr(Id(VAU),[NewExpr(Id(VAU),[])]),BinaryOp(+,IntLit(1),IntLit(2)),FieldAccess(Id(C),Id(@VAU))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 397))


    def test_98(self):
        input = """class Program {
                const x : [5]int = [1,2,3/2,1.0*7];
            } """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(ConstDecl(Id(x),ArrayType(5,IntType),[IntLit(1),IntLit(2),BinaryOp(/,IntLit(3),IntLit(2)),BinaryOp(*,FloatLit(1.0),IntLit(7))]))])])"
        self.assertTrue(TestAST.test(input, expect, 398))


    def test_99(self):
        input = """class A6 <- _S9{
            var t,@3,@0_: [86]string;
            func constructor (_:_){}
            func constructor (){}
            func constructor (){} 
        }class A6{
            var t,@3,@0_: [86]string;
        }"""
        expect = "Program([ClassDecl(Id(_S9),Id(A6),[AttributeDecl(VarDecl(Id(t),ArrayType(86,StringType))),AttributeDecl(VarDecl(Id(@3),ArrayType(86,StringType))),AttributeDecl(VarDecl(Id(@0_),ArrayType(86,StringType))),MethodDecl(Id(constructor),[Param(Id(_),Id(_))],VoidType,Block([])),MethodDecl(Id(constructor),[],VoidType,Block([])),MethodDecl(Id(constructor),[],VoidType,Block([]))]),ClassDecl(Id(A6),[AttributeDecl(VarDecl(Id(t),ArrayType(86,StringType))),AttributeDecl(VarDecl(Id(@3),ArrayType(86,StringType))),AttributeDecl(VarDecl(Id(@0_),ArrayType(86,StringType)))])])"
        self.assertTrue(TestAST.test(input, expect, 399))