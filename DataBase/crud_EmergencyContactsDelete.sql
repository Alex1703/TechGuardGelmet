USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [dbo].[crud_EmergencyContactsDelete]    Script Date: 13/07/2023 9:00:51 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    ALTER PROC [dbo].[crud_EmergencyContactsDelete] @EmergencyContactsID INT AS BEGIN
DELETE FROM
    dbo.EmergencyContacts
WHERE
    Id = @EmergencyContactsID;

END