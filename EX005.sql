create database redes;

create table alunos(
id integer,
nome varchar(40),
bairro varchar(20),
turma varchar(10),
salario decimal(9,2),
datanasc date,
primary key(id));

insert into alunos values (1, 'Ana Pereira', 'Centro', '1ºSemestre', 2000, '1990/10/12');
insert into alunos values (2, 'Bruna Silva', 'Vila Aurora', '2ºSemestre', 1600, '1992/09/09');
insert into alunos values (3, 'Carlos Coelho', 'Conjunto São José', '3ºSemestre', 1850, '1989/08/02');
insert into alunos values (4, 'Denis Rodrigues', 'Centro', '1ºSemestre', 2600, '1998/12/22');
insert into alunos values (5, 'Ellen Rocha', 'Vila Aurora', '1ºSemestre', 900, '1997/09/29');
insert into alunos values (6, 'Fernando Graske', 'Jadrim Atlântico', '2ºSemestre', 1200, '1988/06/11');
insert into alunos values (7, 'Gabriela Silveira', 'Vila Aurora', '4ºSemestre', 2600, '1992/05/06');
insert into alunos values (8, 'Hélio de Penã', 'Centro', '1ºSemestre', 1600, '1995/06/04');
insert into alunos values (9, 'Igor José', 'Conjunto São José', '2ºSemestre', 1300, '1990/12/17');
insert into alunos values (10, 'Júlio Cezar', 'Centro', '1ºSemestre', 1000, '1996/02/16');
insert into alunos values (11, 'Kelly Coutinho', 'Conjunto São José', '1ºSemestre', 1250, '1998/03/06');
insert into alunos values (12, 'Laís Pereira', 'Conjunto São José', '3ºSemestre', 2600, '2000/06/23');
insert into alunos values (13, 'Mariana Barcelos', 'Vila Aurora', '4ºSemestre', 1850, '2001/04/19');
insert into alunos values (14, 'Nadir Pereira', 'Jadrim Atlântico', '3ºSemestre', 1600, '1996/09/21');
insert into alunos values (15, 'Osvaldo Snatos', 'Vila Aurora', '2ºSemestre', 1350, '1994/08/06');
insert into alunos values (16, 'Pedro Luis Pereira', 'Centro', '1ºSemestre', 1100, '1993/09/02');
insert into alunos values (17, 'Roberto Campos', 'Vila Aurora', '2ºSemestre', 1900, '1991/04/07');
insert into alunos values (18, 'Saulo Sérgio Santos', 'Jadrim Atlântico', '2ºSemestre', 1650, '1997/01/26');
insert into alunos values (19, 'Thaís Ventura', 'Centro', '1ºSemestre', 2200, '1996/10/27');
insert into alunos values (20, 'Valdir Pereira', 'Jadrim Atlântico', '3ºSemestre', 2000, '1989/11/09');

/* a. Selecionar todos os registros */
SELECT * FROM alunos;

/* b. Selecionar nome e salário dos alunos */
SELECT nome,salario FROM alunos;

/* c. Selecionar os alunos que moram no centro */
SELECT nome FROM alunos WHERE bairro='Centro';

/* d. Selecionar os alunos de 2º Semestre com salário superior a R$2000,00 */
SELECT nome FROM alunos WHERE turma='2ºSemestre' AND salario>2000;

/* e. Selecionar os alunos das turmas de 2º ou 4º Semestre */
SELECT nome FROM alunos WHERE turma='2ºSemestre' OR turma='4ºSemestre';

/* f. Selecionar os alunos que o nome contenha Pereira */
SELECT nome FROM alunos WHERE nome like'%Pedro%';

/* g. Selecionar os alunos que o nome inicie com a Letra A */
SELECT nome FROM alunos WHERE nome like'A%';

/* h. Selecionar os alunos nascidos em 1990 */
SELECT nome FROM alunos WHERE datanasc like'1990%';

/* i. Selecionar os alunos nascidos entre 1990 e 1994 */
SELECT nome FROM alunos WHERE year(datanasc) between 1990 and 1994;

/* j. Somar o salário dos alunos */
SELECT sum(salario) FROM alunos;

/* k. Calcular o salario médio dos alunos */
SELECT avg(salario) FROM alunos;

/* l. Contar o numero de alunos que não moram no centro */
SELECT count(nome) FROM alunos WHERE bairro!='Centro';

/* m. Contar os alunos agrupando-os por turma */
SELECT turma,count(turma) FROM alunos GROUP BY turma;

/* n. Selecionar bairro, soma dos salários, numero de alunos agrupados por bairro */
SELECT bairro,sum(salario),count(bairro) FROM alunos GROUP BY bairro;

/* o. Inserir um novo aluno */
insert into alunos values (21, 'Osvaldo Cruz', 'Vera Cruz', '3ºSemestre', 2500, '1989/16/09');

/* p. Aumentar 10% o salario dos alunos do 2ºSemestre */
UPDATE alunos SET salario=salario*1.10 WHERE turma='2ºSemestre';

/* q. Excluir o aluno de matricula 4 */
DELETE FROM alunos WHERE id=4;
