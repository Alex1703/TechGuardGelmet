USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [dbo].[crud_UserUpdate]    Script Date: 13/07/2023 9:03:09 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    ALTER PROC [dbo].[crud_UserUpdate] @UserID INT,
    @FullName varchar(50),
    @NumberPhone varchar(100) AS BEGIN
UPDATE
    [dbo].[User]
SET
    [FullName] = @FullName,
    [NumberPhone] = @NumberPhone
WHERE
    ID = @UserID;

END;