import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='admin', host='127.0.0.1', port=3306, charset='utf8')

#Descomente se quiser desfazer o banco
conn.cursor().execute("DROP DATABASE `projetointerdisciplinar`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `projetointerdisciplinar` DEFAULT CHARSET=utf8;
    USE `projetointerdisciplinar`;

    CREATE TABLE `Categorias`(
        `ID_Categoria` INT(4) NOT NULL AUTO_INCREMENT,
        `Nome_Categoria` VARCHAR(45) NOT NULL,
         PRIMARY KEY(`ID_Categoria`)
    )    ENGINE=InnoDB;
    
    CREATE TABLE `Ingrediente`(
        `ID_Ingrediente` INT(4) NOT NULL AUTO_INCREMENT,
        `Descricao_Ingrediente` VARCHAR(45) NOT NULL,
        `Quantidade_Ingrediente` INT(5) NOT NULL,
        `Unidade_Medida_Ingrediente` VARCHAR(45) NOT NULL,
         PRIMARY KEY (`ID_Ingrediente`)
    )    ENGINE=InnoDB;
    
    CREATE TABLE `Alimento`(
        `ID_Alimento` INT(1) NOT NULL AUTO_INCREMENT,
        `Descricao` VARCHAR(50) NOT NULL,
        `Categorias_ID_Categoria` INT(1) NOT NULL,
         PRIMARY KEY (`ID_Alimento`),
         FOREIGN KEY (Categorias_ID_Categoria) REFERENCES Categorias(ID_Categoria)
    )    ENGINE=InnoDB;

    CREATE TABLE `usuario`(
        `id` VARCHAR(90) NOT NULL,
        `nome` VARCHAR(50) NOT NULL,
        `senha` VARCHAR(20) NOT NULL,
         PRIMARY KEY (`id`)
    )    ENGINE=InnoDB;

    CREATE TABLE `Alimento_has_Ingrediente`(
        `Alimento_ID_Alimento` INT,
        `Alimento_Categorias_ID_Categoria` INT,
        `Ingrediente_ID_Ingrediente` INT,
         FOREIGN KEY (Alimento_ID_Alimento) REFERENCES Alimento(ID_Alimento),
         FOREIGN KEY (Alimento_Categorias_ID_Categoria) REFERENCES Alimento(Categorias_ID_Categoria),
         FOREIGN KEY (Ingrediente_ID_Ingrediente) REFERENCES Ingrediente(ID_Ingrediente)
    )    ENGINE=InnoDB;

    CREATE TABLE `Eventos`(
        `ID_Eventos` INT(4) NOT NULL AUTO_INCREMENT,
        `Nome_Evento` VARCHAR(50) NOT NULL,
         PRIMARY KEY (`ID_Eventos`)
    )    ENGINE=InnoDB;

    CREATE TABLE `Modalidade_Refeicao`(
        `ID_Modalidade_Refeicao` INT(4) NOT NULL AUTO_INCREMENT,
        `Modalidade` VARCHAR(50) NOT NULL,
         PRIMARY KEY (`ID_Modalidade_Refeicao`)
    )    ENGINE=InnoDB;

    CREATE TABLE `Local_RU`(
        `ID_Local_RU` INT(4) NOT NULL AUTO_INCREMENT,
        `Nome_RU` VARCHAR(45) NOT NULL,
        `Local_RU` VARCHAR(45) NOT NULL,
         PRIMARY KEY (`ID_Local_RU`)
    )    ENGINE=InnoDB;

    CREATE TABLE `Dia`(
        `ID_Dia` INT(4) NOT NULL AUTO_INCREMENT,
        `Data` DATE NOT NULL,
        `Dia_Semana` VARCHAR(45) NOT NULL,
        `Precipitacao` FLOAT NOT NULL,
        `Umidade` FLOAT NOT NULL,
        `Vento` FLOAT NOT NULL,
        `Temperatura` FLOAT NOT NULL,
         PRIMARY KEY(`ID_Dia`)
    )    ENGINE=InnoDB;

    CREATE TABLE `Dia_has_Eventos`(
        `Dia_ID_Dia` INT,
        `Eventos_ID_Eventos` INT,
         FOREIGN KEY (Dia_ID_Dia) REFERENCES Dia(ID_Dia),
         FOREIGN KEY (Eventos_ID_Eventos) REFERENCES Eventos(ID_Eventos)
    )    ENGINE=InnoDB;

    CREATE TABLE `Cardapio`(
        `ID_Cardapio` INT NOT NULL AUTO_INCREMENT,
        `Descricao` VARCHAR(100),
        `Local_RU_ID_Local_RU` INT,
         PRIMARY KEY (`ID_Cardapio`),
         FOREIGN KEY (Local_RU_ID_Local_RU) REFERENCES Local_RU(ID_Local_RU)
    )    ENGINE=InnoDB;

    CREATE TABLE `Alimento_has_Cardapio`(
        `Alimento_ID_Alimento` INT,
        `Cardapio_ID_Cardapio` INT,
         FOREIGN KEY (Alimento_ID_Alimento) REFERENCES Alimento(ID_Alimento),
         FOREIGN KEY (Cardapio_ID_Cardapio) REFERENCES Cardapio(ID_Cardapio)
    )    ENGINE=InnoDB;

    CREATE TABLE `Refeicao`(
        `ID_Refeicao` INT NOT NULL AUTO_INCREMENT,
        `Quantidade_por_pratos` INT(5),
        `Modalidade_Refeicao_ID_Modalidade_Refeicao` INT,
        `Local_RU_ID_Local_RU` INT,
        `Cardapio_ID_Cardapio` INT,
         PRIMARY KEY (ID_Refeicao),
         FOREIGN KEY (Modalidade_Refeicao_ID_Modalidade_Refeicao) REFERENCES Modalidade_Refeicao(ID_Modalidade_Refeicao),
         FOREIGN KEY (Local_RU_ID_Local_RU) REFERENCES Local_RU(ID_Local_RU),
         FOREIGN KEY (Cardapio_ID_Cardapio) REFERENCES Cardapio(ID_Cardapio)
    )    ENGINE=InnoDB;

    CREATE TABLE `Refeicao_has_Dia`(
        `Refeicao_ID_Refeicao` INT,
        `Refeicao_Modalidade_Refeicao_ID_Modalidade_Refeicao` INT,
        `Refeicao_Local_RU_ID_Local_RU` INT,
        `Dia_ID_Dia` INT,
         FOREIGN KEY (Refeicao_ID_Refeicao) REFERENCES Refeicao(ID_Refeicao),
         FOREIGN KEY (Refeicao_Modalidade_Refeicao_ID_Modalidade_Refeicao) REFERENCES Refeicao(Modalidade_Refeicao_ID_Modalidade_Refeicao),
         FOREIGN KEY (Refeicao_Local_RU_ID_Local_RU) REFERENCES Refeicao(Local_RU_ID_Local_RU),
         FOREIGN KEY (Dia_ID_Dia) REFERENCES Dia(ID_Dia)
    )    ENGINE=InnoDB; 
'''

conn.cursor().execute(criar_tabelas)

cursor = conn.cursor()
cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Categorias(ID_Categoria, Nome_Categoria) VALUES (%s, %s)',
    [
        (1, 'Principal'),
        (2, 'Vegetariano'),
    ])

cursor.execute('select * from projetointerdisciplinar.Categorias')
print(' ------------ Categorias: ------------ ')
for categoria in cursor.fetchall():
    print(categoria[0], categoria[1])

# Inserção de usuário
cursor = conn.cursor()
cursor.executemany(
    'INSERT INTO projetointerdisciplinar.usuario (id, nome, senha) VALUES (%s, %s, %s)',
    [
        ('tiago', 'Tiago Carlos', 'angels'),
        ('carlos', 'Carlos Batista', 'demons'),
        ('chris', 'Chris Cornell', 'audioslave'),
    ])

cursor.execute('select * from projetointerdisciplinar.usuario')
print(' ------------ Usuários: ------------ ')
for user in cursor.fetchall():
    print(user[0])

# Inserção de alimento
cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Alimento (Descricao, ID_Alimento, Categorias_ID_Categoria) VALUES (%s, %s, %s)',
    [
        ('Strogonoff de Frango', 1, 1),
        ('Lombo Assado ao Molho Madeira', 2, 1),
        ('Fricassê', 3, 1),
        ('Lasanha à Bolonhesa', 4, 1),
        ('Pernil em Cubos Acebolado', 5, 1),
        ('Filé de Peixe à Milanesa', 6, 1)
    ])

cursor.execute('select * from projetointerdisciplinar.Alimento')
print(' ------------ Alimentos: ------------ ')
for alimento in cursor.fetchall():
    print(alimento[0])

#cursor.executemany(
#    'INSERT INTO projetointerdisciplinar.Alimento_has_Ingrediente (Alimento_ID_Alimento, Alimento_Categorias_ID_Categoria, Ingrediente_ID_Ingrediente) VALUES (%s, %s, %s)',
 #   [
  #      (1, 1, 1),
   #     (2, 1, 2),
    #    (3, 1, 3),
     #   (4, 1, 4),
     #   (5, 1, 1),
     #   (6, 1, 2)
   # ])

#cursor.execute('select * from projetointerdisciplinar.Alimento_has_Ingrediente')
#print(' ------------ Teste: ------------ ')
#for lista_ingredientes in cursor.fetchall():
#    print(lista_ingredientes[0])

# Inserção de eventos
cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Eventos (Nome_Evento) VALUES (%s)',
    [
        ('Congresso de Educação Física'),
        ('Olímpiada de Programação - 2020'),
        ('Olímpiada de Programação - 2021'),
        ('Semana da Informática - 2020'),
        ('Semana da Informática - 2021'),
    ])

cursor.execute('select * from projetointerdisciplinar.Eventos')
print(' ------------ Eventos: ------------ ')
for evento in cursor.fetchall():
    print(evento[1])

# Inserção de Modalidades de Refeições
cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Modalidade_Refeicao (Modalidade, ID_Modalidade_Refeicao) VALUES (%s, %s)',
    [
        ('Café da manhã', 1),
        ('Almoço', 2),
        ('Jantar', 3),
    ])

cursor.execute('select * from projetointerdisciplinar.Modalidade_Refeicao')
print(' ------------ Modalidades de Refeções: ------------ ')
for modalidade_refeicao in cursor.fetchall():
    print(modalidade_refeicao[1])

cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Ingrediente (ID_Ingrediente, Descricao_Ingrediente, Quantidade_Ingrediente, Unidade_Medida_Ingrediente) VALUES (%s, %s, %s, %s)',
    [
        (1, 'Açúcar', '50', 'Quilos'),
        (2, 'Sal', ' 80', 'Quilos'),
        (3, 'Molho de tomate', '50', 'Gramas'),
        (4, 'Creme de leite', '25', 'Mililitros'),
    ])

cursor.execute('select * from projetointerdisciplinar.Ingrediente')
print(' ------------ Ingredientes: ------------ ')
for ingrediente in cursor.fetchall():
    print(ingrediente[1])

cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Local_RU (ID_Local_RU, Nome_RU, Local_RU) VALUES (%s, %s, %s)',
    [
        (1, 'Restaurante Estudantil Muzambinho', 'Campus Muzambinho'),
        (2, 'Restaurante Estudantil Poços de Caldas', 'Campus Poços de Calas'),
        (3, 'Restaurante Estudantil Passos', 'Campus Passos'),
        (4, 'Restaurante Estudantil Machado', 'Campus Machado'),
    ])

cursor.execute('select * from projetointerdisciplinar.Local_RU')
print(' ------------ Locais: ------------ ')
for local in cursor.fetchall():
    print(local[0], local[1], local[2])

cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Dia (ID_Dia, Data, Dia_Semana, Precipitacao, Umidade, Vento, Temperatura) VALUES (%s, %s, %s, %s, %s, %s, %s)',
    [
        (1, '2021/10/18', 'Segunda-Feira', '60.5', '91', '5', '22'),
        (2, '2021/10/19', 'Terça-Feira', '50.5', '95', '3', '21'),
    ])

cursor.execute('select * from projetointerdisciplinar.Dia')
print(' ------------ Dias: ------------ ')
for dia in cursor.fetchall():
    print(dia[0], dia[1], dia[2], dia[3], dia[4], dia[5], dia[6])

cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Cardapio (ID_Cardapio, Descricao) VALUES (%s, %s)',
    [
        (1, 'Cardápio IFSULDEMINAS - Campus Muzambinho'),
        (2, 'Cardápio IFSULDEMINAS - Campus Poços de Caldas'),
    ])

cursor.execute('select * from projetointerdisciplinar.Cardapio')
print('----------- Cardápios: ------------- ')
for cardapio in cursor.fetchall():
    print(cardapio[0], cardapio[1])

cursor.executemany(
    'INSERT INTO projetointerdisciplinar.Refeicao (ID_Refeicao, Quantidade_por_pratos) VALUES (%s, %s)',
    [
        (1, '2'),
        (2, '5'),
    ])

cursor.execute('select * from projetointerdisciplinar.Refeicao')
print('----------- Refeições: ------------- ')
for refeicao in cursor.fetchall():
    print(refeicao[0], refeicao[1])

# Commitando senão nada tem efeito
conn.commit()
cursor.close()

