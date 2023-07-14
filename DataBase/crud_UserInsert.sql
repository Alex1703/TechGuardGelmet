USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [dbo].[crud_UserInsert]    Script Date: 13/07/2023 9:02:46 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    ALTER PROCEDURE [dbo].[crud_UserInsert] (
        @FullName varchar(50),
        @NumberPhone varchar(100)
    ) AS
SET
    NOCOUNT ON
SET
    XACT_ABORT ON BEGIN TRANSACTION
INSERT INTO
    [dbo].[User] ([FullName], [NumberPhone])
VALUES
    (@FullName, @NumberPhone) DECLARE @UserID INT;

SET
    @UserID = SCOPE_IDENTITY()
SELECT
    *
FROM
    [dbo].[User]
WHERE
    Id = @UserID COMMIT
