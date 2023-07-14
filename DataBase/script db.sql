create database TechGuardGelmet

Use TechGuardGelmet

Create Table [User]
(
	Id int primary key identity(1,1),
	FullName varchar(50),
	NumberPhone varchar(100)
)

create table EmergencyContacts 
(
	Id int primary key identity(1,1),
	[Name] varchar(50),
	NumberPhone varchar(100),
	Fk_User int foreign key references [User] (Id)
)