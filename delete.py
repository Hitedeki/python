use ApiFaces

go 

--deletando colunas
--Alter table rostos drop column grupo

--Adicionando colunas
--alter table rostos add grupo int;

delete from rostos where idArquivo IS NULL
