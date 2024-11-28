-- Inserindo registros na tabela `addresses`
INSERT INTO `addresses` (`state`, `city`, `neighborhood`, `street`, `number`) VALUES
('SP', 'São Paulo', 'Centro', 'Rua A', '123'),
('RJ', 'Rio de Janeiro', 'Copacabana', 'Rua B', '456'),
('MG', 'Belo Horizonte', 'Savassi', 'Rua C', '789'),
('BA', 'Salvador', 'Pelourinho', 'Rua D', '101'),
('PR', 'Curitiba', 'Batel', 'Rua E', '202'),
('RS', 'Porto Alegre', 'Moinhos de Vento', 'Rua F', '303'),
('SC', 'Florianópolis', 'Centro', 'Rua G', '404'),
('PE', 'Recife', 'Boa Viagem', 'Rua H', '505'),
('CE', 'Fortaleza', 'Meireles', 'Rua I', '606'),
('AM', 'Manaus', 'Centro', 'Rua J', '707'),
('PA', 'Belém', 'Cidade Velha', 'Rua K', '808'),
('GO', 'Goiânia', 'Setor Bueno', 'Rua L', '909'),
('ES', 'Vitória', 'Jardim Camburi', 'Rua M', '110'),
('RN', 'Natal', 'Ponta Negra', 'Rua N', '220'),
('AL', 'Maceió', 'Pajuçara', 'Rua O', '330'),
('MA', 'São Luís', 'Centro', 'Rua P', '440'),
('TO', 'Palmas', 'Plano Diretor', 'Rua Q', '550'),
('MT', 'Cuiabá', 'Centro', 'Rua R', '660'),
('MS', 'Campo Grande', 'Centro', 'Rua S', '770'),
('RO', 'Porto Velho', 'Centro', 'Rua T', '880');

-- Inserindo registros na tabela `clients`
INSERT INTO `clients` (`name`, `email`, `address_id`) VALUES
('Alice', 'alice@example.com', 1),
('Bob', 'bob@example.com', 2),
('Carol', 'carol@example.com', 3),
('Dave', 'dave@example.com', 4),
('Eve', 'eve@example.com', 5),
('Frank', 'frank@example.com', 6),
('Grace', 'grace@example.com', 7),
('Hank', 'hank@example.com', 8),
('Ivy', 'ivy@example.com', 9),
('Jack', 'jack@example.com', 10),
('Kim', 'kim@example.com', 11),
('Liam', 'liam@example.com', 12),
('Mia', 'mia@example.com', 13),
('Noah', 'noah@example.com', 14),
('Olivia', 'olivia@example.com', 15),
('Paul', 'paul@example.com', 16),
('Quinn', 'quinn@example.com', 17),
('Ruby', 'ruby@example.com', 18),
('Steve', 'steve@example.com', 19),
('Tina', 'tina@example.com', 20);

-- Inserindo registros na tabela `orders`
INSERT INTO `orders` (`description`, `datetime`, `client_id`) VALUES
('Order 1 description', '2024-11-01 10:00:00', 1),
('Order 2 description', '2024-11-02 11:00:00', 1),
('Order 3 description', '2024-11-03 12:00:00', 2),
('Order 4 description', '2024-11-04 13:00:00', 2),
('Order 5 description', '2024-11-05 14:00:00', 3),
('Order 6 description', '2024-11-06 15:00:00', 4),
('Order 7 description', '2024-11-07 16:00:00', 4),
('Order 8 description', '2024-11-08 17:00:00', 5),
('Order 9 description', '2024-11-09 18:00:00', 6),
('Order 10 description', '2024-11-10 19:00:00', 6),
('Order 11 description', '2024-11-11 20:00:00', 7),
('Order 12 description', '2024-11-12 21:00:00', 7),
('Order 13 description', '2024-11-13 22:00:00', 8),
('Order 14 description', '2024-11-14 23:00:00', 8),
('Order 15 description', '2024-11-15 09:00:00', 9),
('Order 16 description', '2024-11-16 08:00:00', 9),
('Order 17 description', '2024-11-17 07:00:00', 10),
('Order 18 description', '2024-11-18 06:00:00', 10),
('Order 19 description', '2024-11-19 05:00:00', 11),
('Order 20 description', '2024-11-20 04:00:00', 11);

-- Inserindo registros na tabela `products`
INSERT INTO `products` (`name`, `price`) VALUES
('Product A', 10.00),
('Product B', 20.00),
('Product C', 30.00),
('Product D', 40.00),
('Product E', 50.00),
('Product F', 60.00),
('Product G', 70.00),
('Product H', 80.00),
('Product I', 90.00),
('Product J', 100.00),
('Product K', 110.00),
('Product L', 120.00),
('Product M', 130.00),
('Product N', 140.00),
('Product O', 150.00),
('Product P', 160.00),
('Product Q', 170.00),
('Product R', 180.00),
('Product S', 190.00),
('Product T', 200.00);

-- Inserindo registros na tabela `order_product`
INSERT INTO `order_product` (`order_id`, `product_id`) VALUES
(1, 1), (1, 2), (1, 3),
(2, 4), (2, 5),
(3, 6), (3, 7),
(4, 8), (4, 9),
(5, 10), (5, 11),
(6, 12), (6, 13),
(7, 14), (7, 15),
(8, 16), (8, 17),
(9, 18), (9, 19),
(10, 20), (10, 1),
(11, 2), (11, 3), (11, 4),
(12, 5), (12, 6),
(13, 7), (13, 8),
(14, 9), (14, 10),
(15, 11), (15, 12),
(16, 13), (16, 14),
(17, 15), (17, 16),
(18, 17), (18, 18),
(19, 19), (19, 20),
(20, 1), (20, 2);