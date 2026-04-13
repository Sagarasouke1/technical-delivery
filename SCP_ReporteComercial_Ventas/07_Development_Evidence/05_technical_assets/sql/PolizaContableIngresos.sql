WITH src AS (
	SELECT 
		CP.fecha_creacion,
		CP.identificador_poliza AS Poliza,
		CPD.num_partida         AS Partida,
		CPD.centrocosto         AS CentroCosto,
		CPD.referencia          AS Referencia,
		CPD.concepto_individual AS ConceptoMov,
		CPD.mm_cargo            AS Cargo,
		CPD.mm_abono            AS Abono,
		CP.fecha_ingreso,
		CP.fecha_modifico,
		id_tipo_poliza,
		ROW_NUMBER() OVER (
			PARTITION BY CPD.referencia, CPD.concepto_individual, CPD.mm_abono
			ORDER BY CP.fecha_ingreso DESC, CP.fecha_modifico DESC, CP.id_poliza DESC
		) AS rn
	FROM cont_polizadet CPD
	LEFT JOIN cont_poliza CP 
		ON CP.id_poliza = CPD.id_poliza
	WHERE 
		YEAR(CP.fecha_creacion) = YEAR(GETDATE())
		-- AND MONTH(CP.fecha_creacion) = 2
		AND CPD.mm_abono <> 0
		AND CPD.id_centrocosto <> 0
		AND id_tipo_poliza <> 1
)
SELECT 
    fecha_creacion,Poliza,Partida,CentroCosto,Referencia,ConceptoMov,Cargo,Abono,fecha_ingreso,fecha_modifico
FROM src
WHERE rn = 1
ORDER BY fecha_creacion ASC;