USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [dbo].[crud_UserRead]    Script Date: 13/07/2023 9:02:58 p. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
    ALTER PROC [dbo].[crud_UserRead] @UserID int AS BEGIN
SELECT
    [FullName],
    [NumberPhone]
FROM
    [dbo].[User]
WHERE
    ID = @UserID
END
