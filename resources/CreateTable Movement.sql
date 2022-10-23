CREATE TABLE Movements (
    Id int NOT NULL,
    MovementType int NOT NULL,
    MaterialQuantity int NOT NULL,
	Hour Datetime,
	MovementId int,
    CONSTRAINT PK_Movements PRIMARY KEY (Id),
    CONSTRAINT FK_Movements_Movements_MovementId FOREIGN KEY (MovementId) REFERENCES Movements(Id)
);