USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [dbo].[crud_EmergencyContactsUpdate]    Script Date: 13/07/2023 9:02:09 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    ALTER PROC [dbo].[crud_EmergencyContactsUpdate] @EmergencyContactsID INT,
    @Name varchar(50),
    @NumberPhone varchar(100),
    @Fk_User int AS BEGIN
UPDATE
    dbo.EmergencyContacts
SET
    [Name] = @Name,
    [NumberPhone] = @NumberPhone,
    [Fk_User] = @Fk_User
WHERE
    ID = @EmergencyContactsID;

END;