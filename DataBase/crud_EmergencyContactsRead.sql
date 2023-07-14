USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [dbo].[crud_EmergencyContactsRead]    Script Date: 13/07/2023 9:01:58 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    ALTER PROC [dbo].[crud_EmergencyContactsRead] @EmergencyContactsID int AS BEGIN
SELECT
    [Name],
    [NumberPhone],
    [Fk_User]
FROM
    dbo.EmergencyContacts
WHERE
    ID = @EmergencyContactsID
END
