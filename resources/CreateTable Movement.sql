DROP TABLE Movements;
CREATE TABLE Movements (
    Id int NOT NULL IDENTITY(1,1),
    MovementType nText NOT NULL,
    MaterialQuantity int NOT NULL,
	Date Date,
	MaterialId int,
    CONSTRAINT PK_Movements PRIMARY KEY (Id),
    CONSTRAINT FK_Movements_Movements_MaterialId FOREIGN KEY (MaterialId) REFERENCES Materials(Id)
);
