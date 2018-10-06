create database examdb;
use examdb;

create table users_tb
(
	userid varchar(20) primary key,
	password varchar(20),
	firstname varchar(20),
	lastname varchar(20),
	dob varchar(20),
	gender varchar(20),
	address varchar(20),
	contact varchar(20),
	email varchar(200)
);
create table questions_tb
(
	questionid varchar(20) primary key,
	question varchar(200),
	option1 varchar(100),
	option2 varchar(100),
	option3 varchar(100),
	option4 varchar(100),
	coption varchar(100),
	sid varchar(20)
);
create table results_tb
(
	examid varchar(20) primary key,
	uid varchar(20),
	subid varchar(20),
	dateodexam varchar(20),
	noq int,
	cans int,
	per int
);
create table tempans_tb
(
	uans varchar(100)
);
create table subjects_tb
(
	subid varchar(20) primary key,
	subname varchar(100)
);
insert into subjects_tb values('sub001','c++');
insert into subjects_tb values('sub002','java');
insert into subjects_tb values('sub003','python');
insert into subjects_tb values('sub004','c');
insert into questions_tb values
(
	'q0001',
	'Who is the founder of c++?',
	'Denise Ritche',
	'Bjarne Stourstrup',
	'Bill Gates',
	'Mark Zukarburg',
	'Bjarne Stourstrup',
	'sub001'
);
insert into questions_tb values
(
	'q0002',
	'Which of the following type of class allows only one object of it to be created?',
	'Virtual class',
	'Abstract class',
	'Singleton class',
	'Friend class',
	'Singleton class',
	'sub001'
);
insert into questions_tb values
(
	'q0003',
	'Which of the following is not a type of constructor?',
	'Copy constructor',
	'Friend constructor',
	'Default constructor',
	'Parameterized constructor',
	'Friend constructor',
	'sub001'
);
insert into questions_tb values
(
	'q0004',
	'Which of the following statements is correct?',
	'Base class pointer cannot point to derived class',
	'Derived class pointer cannot point to base class',
	'Pointer to derived class cannot be created',
	'Pointer to base class cannot be created',
	'Derived class pointer cannot point to base class',
	'sub001'
);
insert into questions_tb values
(
	'q0005',
	'Which of the following is not the member of class?',
	'Static function',
	'Friend function',
	'Const function',
	'Virtual function',
	'Friend function',
	'sub001'
);
insert into questions_tb values
(
	'q0006',
	'Which of the following concepts means determining at runtime what method to invoke?',
	'Data hiding',
	'Dynamic Typing',
	'Dynamic binding',
	'Dynamic loading',
	'Dynamic binding',
	'sub001'
);
insert into questions_tb values
(
	'q0007',
	'Which of the following term is used for a function defined inside a class?',
	'Member Variable',
	'Member function',
	'Class function',
	'Classic function',
	'Member function',
	'sub001'
);
insert into questions_tb values
(
	'q0008',
	'How many instances of an abstract class can be created?',
	'1',
	'5',
	'13',
	'0',
	'0',
	'sub001'
);
insert into questions_tb values
(
	'q0009',
	'Which of the following cannot be friend?',
	'Function',
	'Class',
	'Object',
	'Operator function',
	'Object',
	'sub001'
);
insert into questions_tb values
(
	'q0010',
	'How many types of polymorphisms are supported by C++?',
	'1',
	'2',
	'3',
	'4',
	'2',
	'sub001'
);

insert into questions_tb values
(
	'q0011',
	'Which interface does java.util.Hashtable implement?',
	'Java.util.Map',
	'Java.util.List',
	'Java.util.HashTable',
	'Java.util.Collection',
	'Java.util.Map',
	'sub002'
);
insert into questions_tb values
(
	'q0012',
	'Which interface provides the capability to store objects using a key-value pair?',
	'Java.util.HashTable',
	'Java.util.List',
	'Java.util.Map',
	'Java.util.Collection',
	'Java.util.Map',
	'sub002'
);
insert into questions_tb values
(
	'q0013',
	'Which is valid declaration of a float?',
	'float f = 1F',
	'float f = 1.0',
	'float f = (1)',
	'float f = 1.0d',
	'float f = 1F',
	'sub002'
);
insert into questions_tb values
(
	'q0014',
	'What is the numerical range of char?',
	'0 to 32767',
	'0 to 65535',
	'-256 to 255',
	'-32768 to 32767',
	'0 to 65535',
	'sub002'
);
insert into questions_tb values
(
	'q0015',
	'Which is true about a method-local inner class?',
	'It must be marked final',
	'It can be marked abstract',
	'It can be marked public',
	'It can be marked static',
	'It can be marked abstract',
	'sub002'
);
insert into questions_tb values
(
	'q0016',
	'What is the name of the method used to start a thread execution?',
	'init()',
	'start()',
	'run()',
	'resume()',
	'start()',
	'sub002'
);
insert into questions_tb values
(
	'q0017',
	'Which of the following will directly stop the execution of a Thread?',
	'wait()',
	'notify()',
	'notifyall()',
	'exits synchronized code',
	'wait()',
	'sub002'
);
insert into questions_tb values
(
	'q0018',
	'Which will contain the body of the thread?',
	'run()',
	'start()',
	'stop()',
	'main()',
	'run()',
	'sub002'
);
insert into questions_tb values
(
	'q0019',
	'Which method registers a thread in a thread scheduler?',
	'run()',
	'construct()',
	'start()',
	'register()',
	'start()',
	'sub002'
);
insert into questions_tb values
(
	'q0020',
	'Which of the following will not directly cause a thread to stop?',
	'notify()',
	'wait()',
	'InputStream access',
	'sleep()',
	'notify()',
	'sub002'
);
insert into questions_tb values
(
	'q0021',
	'Which of these in not a core datatype?',
	'Lists',
	'Dictionary',
	'Tuples',
	'Class',
	'Class',
	'sub003'
);
insert into questions_tb values
(
	'q0022',
	'What is the return type of function id ?',
	'int',
	'float',
	'bool',
	'dict',
	'int',
	'sub003'
);
insert into questions_tb values
(
	'q0023',
	'In order to store values in terms of key and value we use what core datatype?',
	'List',
	'tuple',
	'class',
	'dictionary',
	'dictionary',
	'sub003'
);
insert into questions_tb values
(
	'q0024',
	'What is the return value of trunc() ?',
	'int',
	'bool',
	'float',
	'None',
	'int',
	'sub003'
);
insert into questions_tb values
(
	'q0025',
	'What is answer of this expression, 22 % 3 is?',
	'7',
	'1',
	'0',
	'5',
	'1',
	'sub003'
);
insert into questions_tb values
(
	'q0026',
	'Is Python case sensitive when dealing with identifiers?',
	'yes',
	'no',
	'sometimes only',
	'none of the mentioned',
	'yes',
	'sub003'
);
insert into questions_tb values
(
	'q0027',
	'Which of the following is an invalid variable?',
	'my_string_1',
	'1st_string',
	'foo',
	'_',
	'1st_string',
	'sub003'
);
insert into questions_tb values
(
	'q0028',
	'All keywords in Python are in ?',
	'lower case',
	'UPPER CASE',
	'Capitalized',
	'none',
	'none',
	'sub003'
);
insert into questions_tb values
(
	'q0029',
	'Which of the following cannot be a variable?',
	'__init__',
	'in',
	'it',
	'on',
	'in',
	'sub003'
);
insert into questions_tb values
(
	'q0030',
	'Which of the following is not a keyword?',
	'eval',
	'assert',
	'nonlocal',
	'pass',
	'eval',
	'sub003'
);
insert into questions_tb values
(
	'q0031',
	'The format identifier %i is also used for _____ data type?',
	'char',
	'int',
	'float',
	'double',
	'int',
	'sub004'
);
insert into questions_tb values
(
	'q0032',
	'Which data type is most suitable for storing a number 65000 in a 32-bit system?',
	'signed short',
	'unsigned short',
	'long',
	'int',
	'unsigned short',
	'sub004'
);
insert into questions_tb values
(
	'q0033',
	'What is the size of an int data type?',
	'4 Bytes',
	'8 Bytes',
	'Depends on the system/compiler',
	'Cannot be determined',
	'Depends on the system/compiler',
	'sub004'
);
insert into questions_tb values
(
	'q0034',
	'What is short int in C programming?',
	'Basic datatype of C',
	'Qualifier',
	'short is the qualifier and int is the basic datatype',
	'Cannot be determined',
	'short is the qualifier and int is the basic datatype',
	'sub004'
);
insert into questions_tb values
(
	'q0035',
	'Which of the following cannot be a variable name in C?',
	'volatile',
	'true',
	'friend',
	'export',
	'volatile',
	'sub004'
);
insert into questions_tb values
(
	'q0036',
	'Which keyword is used to prevent any changes in the variable within a C program?',
	'immutable',
	'mutable',
	'const',
	'volatile',
	'const',
	'sub004'
);
insert into questions_tb values
(
	'q0037',
	'A variable declared in a function can be used in main?',
	'True',
	'False',
	'May be',
	'None of the mentioned',
	'False',
	'sub004'
);
insert into questions_tb values
(
	'q0038',
	'Which of the following declaration is not supported by C?',
	'String str',
	'char *str',
	'float str = 3e2',
	'Both (a) and (c)',
	'String str',
	'sub004'
);
insert into questions_tb values
(
	'q0039',
	'Which of the following declaration is not supported by C?',
	'String str',
	'char *str',
	'float str = 3e2',
	'Both (a) and (c)',
	'String str',
	'sub004'
);
insert into questions_tb values
(
	'q0040',
	'Does logical operators in C language are evaluated with short circuit?',
	'True',
	'False',
	'Depends on the compiler',
	'Depends on the standard',
	'True',
	'sub004'
);








