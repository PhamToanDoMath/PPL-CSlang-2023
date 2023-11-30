import unittest
from test_folder.TestUtils import TestChecker
# from main.CSlang.utils.AST import *
from AST import *

class CheckSuite(unittest.TestCase):
    def test_redeclared_class(self):
        input = """class a {} class b {} class a {}"""
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_redeclared_attribute(self):
        input = """class a {var a:int;var c:int;var c:int;}"""
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_redeclared_class_with_ast(self):
        input = Program([ClassDecl(Id("a"),[]),ClassDecl(Id("b"),[]),ClassDecl(Id("a"),[])])
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_redeclared_param(self):
        input = """
        class Program {
            func getTicket(type : Type, type:string): string{
                return "Premium";
            }
            func @main(): void{}
        }
        """
        expect = "Redeclared Parameter: type"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_redeclared_attribute_with_ast(self):
        input = Program([ClassDecl(Id("a"),[AttributeDecl(VarDecl(Id("a"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType())),AttributeDecl(VarDecl(Id("c"),IntType()))])])
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_405(self):
        input = """
        class Program {
            func getTicket(type : Type): void{
            }
            func @main(): void{
                var x: int = 10 + 20;
                var y: int = 1;
                if(x >= y){
                    x := x + 3;
                }
                else {
                    self.getTicket(new Type());
                }
            }
        }class Type{
            func constructor(){
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_406(self):
        input = """class a {var a,c:int;var c:int;}"""
        expect = "Redeclared Attribute: c"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_407(self):
        input = """class Program {
            func getTicket(type : Type): string{
                return "Premium";
            }
            func getTicket(): void{
            }
            func @main(): void{}
        }class Type{}"""
        expect = "Redeclared Method: getTicket"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_408(self):
        input = """class Program {
            var a: int = 1;
            func getTicket(type : Type): string{
                const a:int = 1;
            }
            func @main(): void{}
        }class Type{}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_409(self):
        input = """class Program {
            func @main(): void{}
            func getTicket(a:int): string{
                var a:int = 1;
            }
        }"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_410(self):
        input = """class Program {
            func getTicket(a:int, a: float): string{
            }
        }"""
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        input = """class Program {
            func @main(): void{}
            func get(a: int): int{
                const a: int = 1;
            }
        }"""
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_412(self):
        input = """class Program {
            func @main(): void{}
            func get(a: int): int{}
            func get1(a: int): int{}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        input = """class Program {
            func @main(): void{}
            func get(b:int): int{
                const a: int =1 ;
            }
            func get1(b: int): int{
                const a: int =1 ;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_414(self):
        input = """class Program {
            var a: int;
            func @main(): void{}
        }
        class Type{
            var a:int;
            func get(b:int): int{
                const a: int =1 ;
            }
            func get1(b: int): int{
                const a: int =1 ;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_415(self):
        input = """class Program {
            var a: int;
            func @main(): void{}
        }
        class Type{
            var Program:int;
            var Type:int;
            func get(b:int): int{
                const get: int =1 ;
            }
            func get1(b: int): int{
                const a: int =1 ;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_416(self):
        input = """
        class Type{
            var Program:int;
            var Type:int;
            func get(b:int): int{
                const get: int =1 ;
            }
            func get1(b: int): int{
                const a: int =1 ;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,416))

    def test_417(self):
        input = """
        class Program{}
        class Type{
            var Program:int;
            var Type:int;
            func get(b:int): int{
                const get: int =1 ;
            }
            func get1(b: int): int{
                const a: int =1 ;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_418(self):
        input = """
        class Program{
            func main(a:int): void{}
        }
        class Type{
            var Program:int;
            var Type:int;
            func get(b:int): int{
                const get: int =1 ;
            }
            func get1(b: int): int{
                const a: int =1 ;
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,418))

    def test_419(self):
        input = """
        class Program{
            func @main(): void{}
        }
        class Parent{}
        class Parent<-Type{
            var Program:int;
            var Type:int;
            func get(b:int): int{
                const get: int =1 ;
            }
            func get1(b: int): int{
                const a: int =1 ;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,419))

    def test_420(self):
        input = """
        class Program{
            func @main(): void{}
        }
        class Parent<-Type{
            var Program:int;
            var Type:int;
            func get(b:int): int{
                const get: int =1 ;
            }
            func get1(b: int): int{
                const a: int =1 ;
            }
        }"""
        expect = "Undeclared Class: Parent"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_421(self):
        input = """
        class Program{
            func @main(): void{}
            func get(b:int): int{
                const get: [5]int = [1,2,3,4,5.0];
            }
        }"""
        expect = "Illegal Array Literal: [IntLit(1),IntLit(2),IntLit(3),IntLit(4),FloatLit(5.0)]"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_422(self):
        input = """
        class Program{
            func @main(): void{}
            func get(b:int): int{
                const get: [5]float = [1,2,3,4,5];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,422))

    def test_423(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 0;
                for i:=1; i < 10; i:=i+1{
                    break;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_424(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 0;
                for i:=1; i < 10; i:=i+1{
                    continue;
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_425(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 0;
                for i:=1; i < 10; i:=i+1{
                }
                continue;
            }
        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_426(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 0;
                for i:=1; i < 10; i:=i+1{
                }
                break;
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,426))

    def test_427(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 0;
                for i:=1; i < 10; i:=i+1{
                    for i:=1; i < 10; i:=i+1{
                        break;
                    }
                }

            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,427))

    def test_428(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 0;
                for i:=1; i < 10; i:=i+1{
                    for i:=1; i < 10; i:=i+1{
                    }
                    break;
                }

            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,428))

    def test_429(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 0;
                break;
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_430(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 0;
                break;
            }
        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_431(self):
        input = """
        class Program{
            func @main(): void{
                const i: int;
            }
        }"""
        expect = "Type Mismatch In Declaration: ConstDecl(Id(i),IntType,None)"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_432(self):
        input = """
        class Program{
            func @main(): void{
                var i: int;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_434(self):
        input = """
        class Program{
            func @main(): void{
                var i: void;
            }
        }"""
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),VoidType)"
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_435(self):
        input = """
        class Program{
            func @main(): void{
                var i: int;
            }
            func foo(a,b: void, b:int):void{
            }
        }"""
        expect = "Type Mismatch In Declaration: VarDecl(Id(a),VoidType)"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_436(self):
        input = """
        class Program{
            func @main(): void{
                const i: void;
            }
        }"""
        expect = "Type Mismatch In Declaration: ConstDecl(Id(i),VoidType,None)"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_437(self):
        input = """
        class Program{
            var i: void;
            func @main(): void{
            }
        }"""
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),VoidType)"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_438(self):
        input = """
        class Program{
            func @main(): void{
                 var i: Base = new Type();
            }
        }class Base{
            func constructor(){}
        }
        class Base<-Type{
            func constructor(){}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_439(self):
        input = """
        class Program{
            func @main(): void{
                 var i: Base = new Type();
            }
        }class Base{
        }
        class Type{
            func constructor(){}
        }"""
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),ClassType(Id(Base)),NewExpr(Id(Type),[]))"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_440(self):
        input = """
        class Program{
            func @main(): void{
                 var i: Base = new Type();
            }
        }class Base{
        }
        class Type{
            func constructor(){}
        }"""
        expect = "Type Mismatch In Declaration: VarDecl(Id(i),ClassType(Id(Base)),NewExpr(Id(Type),[]))"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_441(self):
        input = """
        class Program{
            func @main(): void{
                 var i: float = 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_442(self):
        input = """
        class Program{
            func @main(): void{
                 const a: int = 1.2;
            }
        }"""
        expect = "Type Mismatch In Declaration: ConstDecl(Id(a),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_443(self):
        input = """
        class Program{
            func @main(): void{
                 const a: int = 1;
                 a := 2;
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_444(self):
        input = """
        class Program{
            func @main(): void{
                 const a: Base = new Base();
                 a.ABC := 2;
            }
        }
        class Base{
            const ABC: int = 123;
            func constructor(){
            }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(a),Id(ABC)),IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_445(self):
        input = """
        class Program{
            func @main(): void{
                 const a: Base = new Base();
                 a.ABC := 2;
            }
        }
        class Base{
            var ABC: int = 123;
            func constructor(){
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_446(self):
        input = """
        class Program{
            func @main(): void{
                 const a: Base = new Base();
                 var b: int;
                 b := a.ABC;
            }
        }
        class Base{
            const ABC: int= 1;
            func constructor(){
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,446))

    def test_447(self):
        input = """
        class Program{
            func @main(): void{
                 const a: Base = new Base();
                 var b: int;
                 b := (1+1).ABC;
            }
        }
        class Base{
            const ABC: int= 1;
            func constructor(){
            }
        }"""
        expect = "Type Mismatch In Expression: FieldAccess(BinaryOp(+,IntLit(1),IntLit(1)),Id(ABC))"
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_448(self):
        input = """
        class Program{
            func @main(): void{
                 const a: Base = null;
                 var b: int;
                 b := null.ABC;
            }
        }
        class Base{}"""
        expect = "Type Mismatch In Expression: FieldAccess(NullLiteral(),Id(ABC))"
        self.assertTrue(TestChecker.test(input,expect,448))

    def test_449(self):
        input = """
        class Program{
            func @main(): void{
                 const a: Base = null;
                 var b: int;
                 b := null.ABC;
            }
        }
        class Base{}"""
        expect = "Type Mismatch In Expression: FieldAccess(NullLiteral(),Id(ABC))"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_450(self):
        input = """
        class Program{
            func @main(): void{
                 var a: [5]int = [1,2,3,4,5];
                 a[0] := 2;
            }
        }
        class Base{}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,450))

    def test_451(self):
        input = """
        class Program{
            func @main(): void{
                 var a: [5]int = [1,2,3,4,5];
                 var b: int = 0;
                 b[0] := 2;
            }
        }
        class Base{}"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(b),IntLit(0))"
        self.assertTrue(TestChecker.test(input,expect,451))

    def test_452(self):
        input = """
        class Program{
            func @main(): void{
                 var a: [5]int = [1,2,3,4,5];
                 a[1.0] := 2;
            }
        }
        class Base{}"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input,expect,452))

    def test_453(self):
        input = """
        class Program{
            func @main(): void{
                 var a: [5]int = [1,2,3,4,5];
                 var b: int = a[0];
            }
        }
        class Base{}"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,453))

    def test_454(self):
        input = """
        class Program{
            func @main(): void{
                 var i: Base = new Base(1,2);
                 var i2: Base = new Base();
            }
        }class Base{
            func constructor(){}
            func constructor(a: int, b: float){}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,454))

    def test_455(self):
        input = """
        class Program{
            func @main(): void{
                 var i: Base = new Base(1,2);
                 var i2: Base = new Base();
                 var i3: int = 1 + i2.getInt(1);
            }
        }class Base{
            func getInt(a: int): int{return 5;}
            func constructor(){}
            func constructor(a: int, b: int){}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_456(self):
        input = """
        class Program{
            func @main(): void{
                 var i: float = 3.0;
                 var i2: Base = new Base();
                 var i3: int = 1 + i.getInt(1);
            }
        }class Base{
            func getInt(a: int): void{}
            func constructor(){}
            func constructor(a: int, b: int){}
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(i),Id(getInt),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_457(self):
        input = """
        class Program{
            func @main(): void{
                 var i: float = 3.0;
            }
        }class Base{
            func @getInt(a: int): int{}
            func constructor(){
            }
            func foo(a: int, b: int): void{
                var i3: int = 1 + @getInt(1);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_458(self):
        input = """
        class Program{
            func @main(): void{
                 var i: float = 3.0;
            }
        }class Base{
            func @getInt(a: int): int{}
            func constructor(){
            }
            func foo(a: int, b: int): void{
                var i3: int = 1 + @getInt(1,0);
            }
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(@getInt),[IntLit(1),IntLit(0)])"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_459(self):
        input = """
        class Program{
            func @main(): void{
                 var i: float = 3.0;
            }
        }class Base{
            func @getInt(a: int): int{
                return 2.0;
            }
            func constructor(){
            }
        }"""
        expect = "Type Mismatch In Statement: Return(FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_460(self):
        input = """
        class Program{
            func @main(): void{
                 var i: float = 3.0;
            }
        }class Base{
            func @getInt(a: int): void{
                return;
            }
            func constructor(){
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_461(self):
        input = """
        class Program{
            func @main(): void{
                var i: int =1;
                self.setInt := i;
            }
            func setInt(): void{}
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(setInt)),Id(i))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_462(self):
        input = """
        class Program{
            func @main(): void{
                var i, i2: float =1, 2;
                i := 1.0;
                i2 := 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_463(self):
        input = """
        class Program{
            func @main(): void{
                var i2: [2]float = [3,4];
                i2 := [1,2];
                i2 := [2.0, 3.0];
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_464(self):
        input = """
        class Program{
            func @main(): void{
                var i2: [2]float = [3,4];
                i2 := [1,2,3];
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(i2),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,464))

    def test_465(self):
        input = """
        class Program{
            func @main(): void{
                if(1 == 1){}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_466(self):
        input = """
        class Program{
            func @main(): void{
                if(1){}
            }
        }"""
        expect = "Type Mismatch In Statement: If(IntLit(1),Block([]))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_467(self):
        input = """
        class Program{
            func @main(): void{
                var i,j: int = 1,2;
                if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_468(self):
        input = """
        class Program{
            func @main(): void{
                var i,j: int = 1,2;
                for i := 0; i < 10; i := i + 1 {
                    io.@writeInt(i);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_469(self):
        input = """
        class Program{
            func @main(): void{
                var i,j: int = 1,2;
                for i := 0; 10; i := i + 1 {
                    io.@writeInt(i);
                }
            }
        }"""
        expect = "Type Mismatch In Statement: For(AssignStmt(Id(i),IntLit(0)),IntLit(10),AssignStmt(Id(i),BinaryOp(+,Id(i),IntLit(1))),Block([Call(Id(io),Id(@writeInt),[Id(i)])])])"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_470(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 1;
                self.getInt(5);
            }
            func getInt(a: int): int{
                return 5;
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Self(),Id(getInt),[IntLit(5)])"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_471(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 1;
                self.getInt(5);
            }
            func getInt(a: int): void{
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_472(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 1;
                (1+1).getInt(5);
            }
            func getInt(a: int): void{
            }
        }"""
        expect = "Type Mismatch In Statement: Call(BinaryOp(+,IntLit(1),IntLit(1)),Id(getInt),[IntLit(5)])"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_473(self):
        input = """
        class Program{
            func @main(): void{
                var i: int = 1;
                self.getInt(5.0);
            }
            func getInt(a: int): void{
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Self(),Id(getInt),[FloatLit(5.0)])"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_474(self):
        input = """
        class Program{
            func @main(): void{
                const a : Type1 = new Type2();
                a.b := 1;
                a.a := true;
            }
        }
        class Type1{
            var a : bool;
            func foo(): int{}
        }
        class Type1<-Type2{
            var b : int = 2;
            func foo2(): int{}
            func constructor(){}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,474))

    def test_475(self):
        input = """
        class Program{
            func @main(): void{
                const a : Type1 = new Type2();
                a.a := 1;
                const b : Type1 = new Type1();
                b.a := true;
            }
        }
        class Type1{
            var a : bool;
            func constructor(){}
        }
        class Type1<-Type2{
            var a : int = 2;
            func constructor(){}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_476(self):
        input = """
        class Program{
            func @main(): void{
                const a : Type1 = new Type2();
                const a1: Type1 = new Type1();
                a.foo();
                var b: int = a.foo2(1.0,2.0);
                var c: int = a1.foo2(1,2);
            }
        }
        class Type1{
            func foo(): int{}
            func foo2(a: int, b:int): int{}
            func constructor(){}
        }
        class Type1<-Type2{
            var a : int = 2;
            func foo(): void{}
            func foo2(a: float, b:float): int{}
            func constructor(){}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,476))

    def test_477(self):
        input = """
        class Program{
            func @main(): void{
                const a : Type1 = new Type2();
                const a1: Type1 = new Type1();
                a.foo();
                var b: int = a.foo2(1.0,2.0);
                var c: int = a1.foo2(1.0,2.0);
            }
        }
        class Type1{
            func foo(): int{}
            func foo2(a: float, b:float): int{}
            func constructor(){}
        }
        class Type1<-Type2{
            var a : int = 2;
            func foo(): void{}
            func foo2(a: int, b:int): int{}
            func constructor(){}
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(foo2),[FloatLit(1.0),FloatLit(2.0)])"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_478(self):
        input = """
        class Program{
            func @main(): void{
                const a : Type1 = new Type2();
                const a1: Type1 = new Type1();
                a.foo := 1;
            }
        }
        class Type1{
            func foo(): int{}
            func foo2(a: float, b:float): int{}
            func constructor(){}
        }
        class Type1<-Type2{
            var a : int = 2;
            func foo(): void{}
            func constructor(){}
            func foo2(a: int, b:int): int{}
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Id(a),Id(foo)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_479(self):
        input = """
        class Program{
            func @main(): void{
                const a : float = 1 + 1.0;
                const a1: string = "String" ^ "string";
                const a2: bool = (1 == 1) || true;
                const a3: float = 1.0/1.0;
                const a5, a6: int = 1\\1, 1%1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_480(self):
        input = """
        class Program{
            func @main(): void{
                const a : float = -1 + +1.0;
                const a1: string = "String" ^ "string";
                const a3: float = -1.0/1.0;
                const a4: bool = !true || false || (1==-1);
                const a5 : float = !-1;
            }
        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,UnaryOp(-,IntLit(1)))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_481(self):
        input = """
        class Program{
            func @main(): void{
                const a : Type = new Type2();
            }
        }
        class Type{
        }
        class Type<-Type1{
        }
        class Type1<-Type2{
            func constructor(){}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_482(self):
        input = """
        class Program{
            func @main(): void{
                var a: Type;
            }
        }"""
        expect = "Undeclared Class: Type"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_483(self):
        input = """
        class Program{
            func @main(): void{
                var a: Type = new Type();
            }
        }"""
        expect = "Undeclared Class: Type"
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_484(self):
        input = """
        class Program{
            func @main(): void{}
            func foo(a: Type): void {}
        }"""
        expect = "Undeclared Class: Type"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_485(self):
        input = """
        class Program{
            func @main(): void{}
            var b: int =1;
            func foo(a: Type): void{
                b := 1;
            }
        }
        class Type{}"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_486(self):
        input = """
        class Program{
            func @main(): void{}
            func foo(a: Type): void{
                a.b := 1;
            }
        }
        class Type{
            func constructor(){}
        }"""
        expect = "Undeclared Attribute: b"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_487(self):
        input = """
        class Program{
            func @main(): void{}
            func foo(a: Type): void{
                a.b();
            }
        }
        class Type{
            func constructor(){}
        }"""
        expect = "Undeclared Method: b"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_488(self):
        input = """
        class Program{
            func @main(): void{
                var a: Type = (new Type()).foo();
            }
        }
        class Type{
            func foo(): Type{}
            func constructor(){}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_489(self):
        input = """
        class Program{
            func @main(): void{
                var a: Type = (new Type()).foo();
            }
        }
        class Type{
            func constructor(){}
        }"""
        expect = "Undeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_490(self):
        input = """
        class Program{
            func @main(): void{
                self.foo := 1;
            }
            func foo(): void{
            }
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Self(),Id(foo)),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_491(self):
        input = """
        class Program{
            func @main(): void{
                Type.@foo();
            }
        }"""
        expect = "Undeclared Class: Type"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_492(self):
        input = """
        class Program{
            func @main(): void{
                @foo();
            }
            func @foo(): void{}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_493(self):
        input = """
        class Program{
            func @main(): void{
                var a: int = Type.@foo();
            }
        }"""
        expect = "Undeclared Class: Type"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_494(self):
        input = """
        class Program{
            func @main(): void{
                var a: int = @foo();
            }
            func @foo(): int{}
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_495(self):
        input = """
        class Program{
            func @main(): void{
                var a: int = new Type();
            }
        }"""
        expect = "Undeclared Class: Type"
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_496(self):
        input = """
        class Program{
            func @main(): void{
                var a: int = id.foo();
            }
        }"""
        expect = "Undeclared Identifier: id"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_497(self):
        input = """
        class Program{
            func @main(): void{
                id.foo();
            }
        }"""
        expect = "Undeclared Identifier: id"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_498(self):
        input = """
        class Program{
            func @main(): void{
                var a: int = self.foo();
            }
            var foo: int = 1;
        }"""
        expect = "Type Mismatch In Expression: CallExpr(Self(),Id(foo),[])"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_499(self):
        input = """
        class Program{
            func @main(): void{
                var a: Type = new Type("a", 1, false);
                var b: Type = new Type(1, 1, "string");
            }
        }class Type{
            func constructor(a: int, b: int, c: string){
            }
            func constructor(a: string, b: int, c: bool){
            }
        }"""
        expect = "successful"
        self.assertTrue(TestChecker.test(input,expect,499))

    def test_500(self):
        input = """
        class Program{
            func @main(): void{
                var a: Type = new Type(1, 1, 1);
                var b: Type = new Type1(1, 1, "string");
                var c: Type = new Type1("string", "string", "string");
            }
        }class Type{
            func constructor(a: int, b: int, c: int){
            }
            func constructor(a: string, b: string, c: string){
            }
        }class Type<-Type1{
            func constructor(a: int, b: int, c: string){
            }
            func constructor(a: string, b: int, c: bool){
            }
        }"""
        expect = "Type Mismatch In Expression: NewExpr(Id(Type1),[StringLit(string),StringLit(string),StringLit(string)])"
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_501(self):
        input = """
        class Program{
            func @main(): void{
                var a: Type = new Type(1, 1, 1);
                var b: Type = new Type1(1, 1, "string");
                b.@a := 1;
            }
        }class Type{
            var @a : int = 1;
            func constructor(a: int, b: int, c: int){
            }
            func constructor(a: string, b: string, c: string){
            }
        }class Type<-Type1{
            func constructor(a: int, b: int, c: string){
            }
            func constructor(a: string, b: int, c: bool){
            }
        }"""
        expect = "Undeclared Attribute: @a"
        self.assertTrue(TestChecker.test(input,expect,501))