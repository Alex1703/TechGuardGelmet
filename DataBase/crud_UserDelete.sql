USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [dbo].[crud_UserDelete]    Script Date: 13/07/2023 9:02:24 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    ALTER PROC [dbo].[crud_UserDelete] @UserID INT AS BEGIN
DELETE FROM
    [dbo].[User]
WHERE
    Id = @UserID;

END