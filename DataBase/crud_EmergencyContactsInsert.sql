USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [dbo].[crud_EmergencyContactsInsert]    Script Date: 13/07/2023 9:01:20 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    ALTER PROCEDURE [dbo].[crud_EmergencyContactsInsert] (
        @Name varchar(50),
        @NumberPhone varchar(100),
        @Fk_User int
    ) AS
SET
    NOCOUNT ON
SET
    XACT_ABORT ON BEGIN TRANSACTION
INSERT INTO
    dbo.EmergencyContacts ([Name], [NumberPhone], [Fk_User])
VALUES
    (@Name, @NumberPhone, @Fk_User) DECLARE @EmergencyContactsID INT;

SET
    @EmergencyContactsID = SCOPE_IDENTITY()
SELECT
    *
FROM
    dbo.EmergencyContacts
WHERE
    Id = @EmergencyContactsID COMMIT
