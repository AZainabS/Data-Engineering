PostgreSQL: https://luminousmen.com/post/spark-tips-optimizing-jdbc-data-source-reads
Нужно jar закинуть в ту же директорию в JH, в которой находится ноутбук, в котором запускается спарк, в конфиги спарк сессии добавить 
('spark.jars', 'postgresql-42.5.2.jar')


sdf= (
    spark.read
    .format("jdbc")
    .option("url", f"jdbc:postgresql://host:5432/db")
    .option("user", f"{LOGIN}")
    .option("password", f'{PASSWORD}')
    .option("driver", "org.postgresql.Driver")
    .option("dbschema","db")
    .option("dbtable", f"(SELECT * FROM db.table LIMIT 10)a").load()
    )
