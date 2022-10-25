DROP TABLE Movements;
CREATE TABLE Movements (
    Id int NOT NULL,
    MovementType nText NOT NULL,
    MaterialQuantity int NOT NULL,
	Date Date,
	MovementId int,
    CONSTRAINT PK_Movements PRIMARY KEY (Id),
    CONSTRAINT FK_Movements_Movements_MovementId FOREIGN KEY (MovementId) REFERENCES Movements(Id)
);