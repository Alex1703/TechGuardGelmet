USE [TechGuardGelmet]
GO
/****** Object:  StoredProcedure [[dbo]].[GenerarCRUD]    Script Date: 12/07/2023 8:53:47 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
Alter PROCEDURE [dbo].[GenerarCRUD] (@NameTable NVARCHAR(100))
AS
BEGIN
	
    DECLARE @sql NVARCHAR(MAX)
    
    -- Obtener los nombres de los campos de la tabla
    DECLARE @fields NVARCHAR(MAX)
    SET @fields = STUFF((SELECT ', ' + QUOTENAME(c.name) 
                         FROM sys.columns c
                         WHERE c.object_id = OBJECT_ID(@NameTable)
                         FOR XML PATH('')), 1, 8, '')
    -- Obtener parametros 
	DECLARE @parameters NVARCHAR(MAX)
	SET @parameters = STUFF((	SELECT ',  @'+COLUMN_NAME +' '+ DATA_TYPE + IIF(CONVERT(varchar(100),CHARACTER_MAXIMUM_LENGTH) IS NOT NULL, '('+ CONVERT(varchar(100),CHARACTER_MAXIMUM_LENGTH)+ ')','')
								FROM INFORMATION_SCHEMA.COLUMNS
								WHERE TABLE_SCHEMA = 'dbo' and TABLE_NAME = @NameTable
								ORDER BY ORDINAL_POSITION
                         FOR XML PATH('')), 1, 12, '')
	
	--Obtener valores
	DECLARE @values NVARCHAR(MAX)
	SET @values = STUFF((	SELECT ',  @'+COLUMN_NAME 
								FROM INFORMATION_SCHEMA.COLUMNS
								WHERE TABLE_SCHEMA = 'dbo' and TABLE_NAME = @NameTable
								ORDER BY ORDINAL_POSITION
                         FOR XML PATH('')), 1, 9, '')
	

    -- SP para insertar un registro
    SET @sql =		  ' IF OBJECT_ID(''[dbo].crud_'+ @NameTable+'Insert'') IS NOT NULL'
	SET @sql = @sql + ' BEGIN'
	SET @sql = @sql + '	DROP PROCEDURE [dbo].crud_'+ @NameTable+'Insert'
	SET @sql = @sql + ' END'	
	SET @sql = @sql + ' GO'	
	SET @sql = @sql + ' CREATE PROCEDURE [dbo].crud_'+ @NameTable+'Insert'
	SET @sql = @sql + '	('
	SET @sql = @sql + '		'+@parameters+''
	SET @sql = @sql + '	)'
	SET @sql = @sql + ' AS'
	SET @sql = @sql + '	SET NOCOUNT ON'
	SET @sql = @sql + '	SET XACT_ABORT ON'
	SET @sql = @sql + '	BEGIN TRANSACTION'
	SET @sql = @sql + '	INSERT INTO [dbo].['+ @NameTable+']'
	SET @sql = @sql + '	('
	SET @sql = @sql + '		'+ @fields
	SET @sql = @sql + '	)'
	SET @sql = @sql + '	VALUES'
	SET @sql = @sql + '	('
	SET @sql = @sql + '		'+@values+''
	SET @sql = @sql + '	)'
	SET @sql = @sql + ' DECLARE @'+ @NameTable+'ID INT;'
	SET @sql = @sql + ' SET @'+ @NameTable+'ID = SCOPE_IDENTITY()'
	SET @sql = @sql + '	SELECT *'
	SET @sql = @sql + '	FROM [dbo].['+ @NameTable+']'
	SET @sql = @sql + '	WHERE Id = @'+ @NameTable+'ID'
	SET @sql = @sql + '	COMMIT '
	SET @sql = @sql + '	GO '

	--EXEC (@sql)
	print @sql
    
    -- SP para actualizar un registro
    SET @sql =        ' IF OBJECT_ID(''crud_'+@NameTable+'Update'') IS NOT NULL'
	SET @sql = @sql + ' BEGIN'
	SET @sql = @sql + ' 	DROP PROC'
	SET @sql = @sql + ' 		crud_'+@NameTable+'Update;'
	SET @sql = @sql + ' END '
	SET @sql = @sql + ' GO'
	SET @sql = @sql + ' CREATE PROC crud_'+@NameTable+'Update'
	SET @sql = @sql + ' 	@'+@NameTable+'ID INT,'
	SET @sql = @sql + @parameters
	SET @sql = @sql + ' AS'
	SET @sql = @sql + ' 	BEGIN'
	SET @sql = @sql + ' '
	SET @sql = @sql + ' 		UPDATE [dbo].['+@NameTable+']'
	SET @sql = @sql + '      SET ' + STUFF((SELECT ', ' + QUOTENAME(c.name) + ' = @' + c.name
					 				  FROM sys.columns c
					 				  WHERE c.object_id = OBJECT_ID(@NameTable)
					 				  FOR XML PATH('')), 1, 13, '') + ' '
	SET @sql = @sql + ' 		WHERE ID = @'+@NameTable+'ID;'
	SET @sql = @sql + ' 	END;'
	
    --EXEC(@sql)
	print @sql
    
    -- SP para eliminar un registro
    SET @sql =		  ' IF OBJECT_ID(''crud_'+@NameTable+'Delete'') IS NOT NULL'
	SET @sql = @sql + ' BEGIN'
	SET @sql = @sql + ' 	DROP PROC crud_'+@NameTable+'Delete;'
	SET @sql = @sql + ' END '
	SET @sql = @sql + ' GO'
	SET @sql = @sql + ' CREATE PROC crud_'+@NameTable+'Delete'
	SET @sql = @sql + ' 	@'+@NameTable+'ID INT'
	SET @sql = @sql + ' AS'
	SET @sql = @sql + ' 	BEGIN'
	SET @sql = @sql + ' 		DELETE FROM [dbo].['+@NameTable+']'
	SET @sql = @sql + ' 		WHERE Id = @'+@NameTable+'ID;'
	SET @sql = @sql + ' 	END'
    --EXEC(@sql)
	print @sql
    
    -- SP para obtener todos los registros
    SET @sql = 		  ' IF OBJECT_ID(''crud_'+@NameTable+'ReadById'') IS NOT NULL'
	SET @sql = @sql + ' BEGIN '
	SET @sql = @sql + '     DROP PROC crud_'+@NameTable+'ReadById'
	SET @sql = @sql + ' END '
	SET @sql = @sql + ' GO '
	SET @sql = @sql + ' CREATE PROC crud_'+@NameTable+'Read'
	SET @sql = @sql + '     @'+@NameTable+'ID int'
	SET @sql = @sql + ' AS '
	SET @sql = @sql + ' BEGIN '
	SET @sql = @sql + ' 	SELECT '+@fields
	SET @sql = @sql + ' 	FROM [dbo].['+@NameTable+']'
	SET @sql = @sql + ' 	WHERE ID = @'+@NameTable+'ID'
	SET @sql = @sql + ' END'
	SET @sql = @sql + ' GO '
	--EXEC(@sql)
	print @sql
	
END
