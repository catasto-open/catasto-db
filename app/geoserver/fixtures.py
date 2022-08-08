from datetime import datetime

from app.configs import cnf

from app.geoserver.api import (
    create_workspace,
    create_datastore,
    create_layer,
    get_settings,
    update_settings,
)

workspace = {
    "workspace": {
        "name": cnf.CATASTO_OPEN_GS_WORKSPACE,
        "namespace": {
            "prefix": "CatastoOpenDev",
            "uri": "catasto-open-dev",
            "isolated": False,
        },
    }
}

datastore = {
    "dataStore": {
        "name": cnf.CATASTO_OPEN_GS_DATASTORE,
        "description": cnf.CATASTO_OPEN_GS_DATASTORE,
        "type": "PostGIS",
        "enabled": True,
        "workspace": {
            "name": cnf.CATASTO_OPEN_GS_WORKSPACE,
            "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
            f"/geoserver/rest/workspaces"
            f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
        },
        "connectionParameters": {
            "entry": [
                {"@key": "schema", "$": "public"},
                {"@key": "Evictor run periodicity", "$": "300"},
                {"@key": "Max open prepared statements", "$": "50"},
                {"@key": "encode functions", "$": "True"},
                {"@key": "Batch insert size", "$": "1"},
                {"@key": "preparedStatements", "$": "False"},
                {"@key": "database", "$": cnf.POSTGRES_DB},
                {
                    "@key": "host",
                    "$": f"{cnf.APP_CONFIG.COMPOSE_PROJECT_NAME}-db",
                },
                {"@key": "Loose bbox", "$": "True"},
                {"@key": "SSL mode", "$": "ALLOW"},
                {"@key": "Estimated extends", "$": "True"},
                {"@key": "fetch size", "$": "1000"},
                {"@key": "Expose primary keys", "$": "False"},
                {"@key": "validate connections", "$": "True"},
                {
                    "@key": "Support on the fly geometry simplification",
                    "$": "True",
                },
                {"@key": "Connection timeout", "$": "20"},
                {"@key": "create database", "$": "False"},
                {"@key": "Method used to simplify geometries", "$": "FAST"},
                {"@key": "port", "$": cnf.POSTGRES_CONTAINER_PORT},
                {"@key": "passwd", "$": cnf.POSTGRES_PASS},
                {"@key": "min connections", "$": "1"},
                {"@key": "dbtype", "$": "postgis"},
                {
                    "@key": "namespace",
                    "$": f"http://{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                },
                {"@key": "max connections", "$": "10"},
                {"@key": "Evictor tests per run", "$": "3"},
                {"@key": "Test while idle", "$": "True"},
                {"@key": "user", "$": cnf.POSTGRES_USER},
                {"@key": "Max connection idle time", "$": "300"},
            ]
        },
        "_default": True,
        "featureTypes": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
        f"/geoserver/rest/workspaces"
        f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
        f"/datastores/{cnf.CATASTO_OPEN_GS_DATASTORE}"
        f"/featuretypes.json",
    }
}

layers = [
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER,
            "keywords": {
                "string": ["features", cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER]
            },
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84 / '
                'Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n     '
                ' SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", '
                "NORTH], \n    "
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular '
                'Visualisation Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  '
                'AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": -180.00000000000003,
                "maxx": 180.00000000000003,
                "miny": -85.06,
                "maxy": 85.06,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_CITY_LAYER,
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_COMUNI_.format(
                            "%city%", "%endDate%"
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "city",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "name",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "code",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER,
            "namespace": {
                "name": "CatastoOpenDev",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/namespaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER,
            "keywords": {
                "string": [
                    "features",
                    cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER,
                ]
            },
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84  / Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation Pseudo Mercator"], '
                '\n  PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": -8.9831528412e-6,
                "maxx": 0,
                "miny": -8.983152841e-6,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_SECTION_LAYER,
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_SEZIONI_.format(
                            "%cityCode%", "%endDate%"
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "cityCode",
                                "defaultValue": "H224",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": {
                    "name": "name",
                    "minOccurs": 1,
                    "maxOccurs": 1,
                    "nillable": False,
                    "binding": "java.lang.String",
                }
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER,  # noqa
            "keywords": {
                "string": ["features", cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER]
            },
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84  / Pseudo-Mercator", \n'
                '  GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation '
                'Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  '
                'AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": 1742498.9942617496,
                "maxx": 1744044.2337921541,
                "miny": 4600266.217691349,
                "maxy": 4602063.855741888,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": 15.65313479108224,
                "maxx": 15.667015913960121,
                "miny": 38.147377047518255,
                "maxy": 38.16007548511116,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_SHEET_LAYER,
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_FOGLI.format(
                            "%cityCode%",
                            "%sectionCode%",
                            "%startDate%",
                            "%endDate%",
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "cityCode",
                                "defaultValue": "H224",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "sectionCode",
                                "defaultValue": "A",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "startDate",
                                "defaultValue": "0001-01-01",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                        "geometry": [
                            {
                                "name": "extent",
                                "type": "Polygon",
                                "srid": 3857,
                            },
                            {
                                "name": "geom",
                                "type": "MultiPolygon",
                                "srid": 3857,
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "citycode",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "section",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "sheet",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "number",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "geom",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.MultiPolygon",
                    },
                    {
                        "name": "extent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.Polygon",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER,
            "keywords": {
                "string": [
                    "features",
                    cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER,
                ]
            },
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84  / Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation '
                'Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  '
                'AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": 1743369.7459205368,
                "maxx": 1743379.8221324224,
                "miny": 4600646.325895493,
                "maxy": 4600656.878548826,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": 15.66095688631985,
                "maxx": 15.661047402471278,
                "miny": 38.15006229979151,
                "maxy": 38.15013684698621,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_LAYER,
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_FABBRICATI.format(
                            "%cityCode%",
                            "%sectionCode%",
                            "%citySheet%",
                            "%startDate%",
                            "%endDate%",
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "cityCode",
                                "defaultValue": "H224",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "sectionCode",
                                "defaultValue": "A",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "citySheet",
                                "defaultValue": 2,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "startDate",
                                "defaultValue": "0001-01-01",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                        "geometry": [
                            {
                                "name": "extent",
                                "type": "Polygon",
                                "srid": 3857,
                            },
                            {
                                "name": "geom",
                                "type": "MultiPolygon",
                                "srid": 3857,
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "citycode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "section",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "sheet",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "number",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "geom",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.MultiPolygon",
                    },
                    {
                        "name": "extent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.Polygon",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER,
            "keywords": {
                "string": ["features", cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER]
            },
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84  / Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation '
                'Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": 1742622.802317007,
                "maxx": 1743010.1213810008,
                "miny": 4600654.241552448,
                "maxy": 4601005.713651081,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": 15.654246977765588,
                "maxx": 15.657726324115753,
                "miny": 38.1501182184384,
                "maxy": 38.15260108274686,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_LAND_LAYER,
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_TERRENI.format(
                            "%cityCode%",
                            "%sectionCode%",
                            "%citySheet%",
                            "%startDate%",
                            "%endDate%",
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "cityCode",
                                "defaultValue": "H224",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "sectionCode",
                                "defaultValue": "A",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "citySheet",
                                "defaultValue": 2,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "startDate",
                                "defaultValue": "0001-01-01",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                        "geometry": [
                            {
                                "name": "extent",
                                "type": "Polygon",
                                "srid": 3857,
                            },
                            {
                                "name": "geom",
                                "type": "MultiPolygon",
                                "srid": 3857,
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "citycode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "section",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "sheet",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "number",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "geom",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.MultiPolygon",
                    },
                    {
                        "name": "extent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.Polygon",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
            "keywords": {
                "string": [
                    "features",
                    cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,
                ]
            },
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n    '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_NATURAL_SUBJECT_LAYER,  # noqa
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_PERSONE_FISICA.format(
                            "%fiscalCode%", "%lastName%", "%firstName%"
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {"name": "fiscalCode", "defaultValue": "null"},
                            {"name": "lastName", "defaultValue": "null"},
                            {"name": "firstName", "defaultValue": "null"},
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "subjects",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "subjecttype",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "firstname",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "lastname",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "fiscalcode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "dateofbirth",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                    {
                        "name": "cityofbirth",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "gender",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
            "keywords": {
                "string": [
                    "features",
                    cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,
                ]
            },
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n   '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_LEGAL_SUBJECT_LAYER,  # noqa
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_NON_FISICA.format(
                            "%vatNumber%", "%businessName%"
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {"name": "businessName", "defaultValue": "null"},
                            {"name": "vatNumber", "defaultValue": "null"},
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "subjects",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "subjecttype",
                        "minOccurs": 1,
                        "maxOccurs": 1,
                        "nillable": False,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "businessname",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "vatnumber",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "branch",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER,
            "keywords": {
                "string": [
                    "features",
                    cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER,
                ]
            },
            "nativeCRS": {
                "@class": "projected",
                "$": 'PROJCS["WGS 84 / Pseudo-Mercator", \n  '
                'GEOGCS["WGS 84", \n    '
                'DATUM["World Geodetic System 1984", \n      '
                'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
                'AUTHORITY["EPSG","7030"]], \n      '
                'AUTHORITY["EPSG","6326"]], \n    '
                'PRIMEM["Greenwich", 0.0, '
                'AUTHORITY["EPSG","8901"]], \n    '
                'UNIT["degree", 0.017453292519943295], \n    '
                'AXIS["Geodetic longitude", EAST], \n    '
                'AXIS["Geodetic latitude", NORTH], \n    '
                'AUTHORITY["EPSG","4326"]], \n  '
                'PROJECTION["Popular Visualisation '
                'Pseudo Mercator"], \n  '
                'PARAMETER["semi_minor", 6378137.0], \n  '
                'PARAMETER["latitude_of_origin", 0.0], \n  '
                'PARAMETER["central_meridian", 0.0], \n  '
                'PARAMETER["scale_factor", 1.0], \n  '
                'PARAMETER["False_easting", 0.0], \n  '
                'PARAMETER["False_northing", 0.0], \n  '
                'UNIT["m", 1.0], \n  '
                'AXIS["Easting", EAST], \n  '
                'AXIS["Northing", NORTH], \n  '
                'AUTHORITY["EPSG","3857"]]',
            },
            "srs": "EPSG:3857",
            "nativeBoundingBox": {
                "minx": 1742622.802317007,
                "maxx": 1743869.270019752,
                "miny": 4600654.241552448,
                "maxy": 4602022.954962236,
                "crs": {"@class": "projected", "$": "EPSG:3857"},
            },
            "latLonBoundingBox": {
                "minx": 15.654246977765588,
                "maxx": 15.66544418765096,
                "miny": 38.1501182184384,
                "maxy": 38.15978658835018,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_SUBJECT_PROPERTY_LAYER,  # noqa
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_SOGGETTI.format(
                            "%subjects%",
                            "%subjectType%",
                            "%startDate%",
                            "%endDate%",
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "subjects",
                                "defaultValue": "1,2",
                                "regexpValidator": "^([0-9]+,)*[0-9]+$",
                            },
                            {
                                "name": "subjectType",
                                "defaultValue": "P",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "startDate",
                                "defaultValue": "0001-01-01",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                        "geometry": [
                            {
                                "name": "extent",
                                "type": "Polygon",
                                "srid": 3857,
                            },
                            {
                                "name": "geom",
                                "type": "MultiPolygon",
                                "srid": 3857,
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "citycode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "section",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "sheet",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "number",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "geom",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.MultiPolygon",
                    },
                    {
                        "name": "extent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "org.locationtech.jts.geom.Polygon",
                    },
                    {
                        "name": "city",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "subordinate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "right",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "part",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "classification",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "class",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "consistency",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "income",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "lot",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "propertytype",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "startdate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                    {
                        "name": "enddate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER,
            "keywords": {
                "string": [
                    "features",
                    cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER,
                ]
            },
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n    '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_PROPERTY_OWNER_LAYER,  # noqa
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_TITOLARI_IMMOBILE.format(  # noqa
                            "%cityCode%",
                            "%property%",
                            "%propertyType%",
                            "%startDate%",
                            "%endDate%",
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "cityCode",
                                "defaultValue": "H224",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "property",
                                "defaultValue": 315,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "propertyType",
                                "defaultValue": "T",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "startDate",
                                "defaultValue": "0001-01-01",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "nominative",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "fiscalcode",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "city",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "right",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "part",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "startdate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                    {
                        "name": "enddate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER,
            "keywords": {
                "string": [
                    "features",
                    cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER,
                ]
            },
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n    '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -1,
                "maxx": 0,
                "miny": -1,
                "maxy": 0,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -85,
                "maxy": 85,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_LAND_DETAIL_LAYER,
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_TERENNO_DETAIL.format(
                            "%cityCode%",
                            "%citySheet%",
                            "%landNumber%",
                            "%startDate%",
                            "%endDate%",
                        ),
                        "escapeSql": True,
                        "parameter": [
                            {
                                "name": "cityCode",
                                "defaultValue": "H224",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "citySheet",
                                "defaultValue": 2,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "landNumber",
                                "defaultValue": "00005",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "startDate",
                                "defaultValue": "0001-01-01",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": True,
            "simpleConversionEnabled": True,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": True,
            "forcedDecimal": True,
            "overridingServiceSRS": True,
            "skipNumberMatched": True,
            "circularArcPresent": True,
            "attributes": {
                "attribute": [
                    {
                        "name": "property",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Long",
                    },
                    {
                        "name": "propertytype",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "subordinate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "quality",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "class",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "hectares",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "are",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "centiare",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Integer",
                    },
                    {
                        "name": "lot",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "cadastralrent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "agriculturalrent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "startdate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                    {
                        "name": "enddate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                ]
            },
        }
    },
    {
        "featureType": {
            "name": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER,
            "nativeName": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER,
            "namespace": {
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}",
                "href": f"{cnf.GEOSERVER_HOST}:"
                f"{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest/namespaces"
                f"/{cnf.CATASTO_OPEN_GS_WORKSPACE}.json",
            },
            "title": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER,
            "keywords": {
                "string": [
                    "features",
                    cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER,
                ]
            },
            "nativeCRS": 'GEOGCS["WGS 84", \n  '
            'DATUM["World Geodetic System 1984", \n    '
            'SPHEROID["WGS 84", 6378137.0, 298.257223563, '
            'AUTHORITY["EPSG","7030"]], \n    '
            'AUTHORITY["EPSG","6326"]], \n  '
            'PRIMEM["Greenwich", 0.0, '
            'AUTHORITY["EPSG","8901"]], \n  '
            'UNIT["degree", 0.017453292519943295], \n  '
            'AXIS["Geodetic longitude", EAST], \n  '
            'AXIS["Geodetic latitude", NORTH], \n  '
            'AUTHORITY["EPSG","4326"]]',
            "srs": "EPSG:4326",
            "nativeBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "latLonBoundingBox": {
                "minx": -180,
                "maxx": 180,
                "miny": -90,
                "maxy": 90,
                "crs": "EPSG:4326",
            },
            "projectionPolicy": "FORCE_DECLARED",
            "enabled": True,
            "metadata": {
                "entry": {
                    "@key": "JDBC_VIRTUAL_TABLE",
                    "virtualTable": {
                        "name": cnf.APP_CONFIG.CATASTO_OPEN_BUILDING_DETAIL_LAYER,  # noqa
                        "sql": cnf.APP_CONFIG.VIEW_QUERY_FABBRICATI_DETAIL.format(  # noqa
                            "%cityCode%",
                            "%citySheet%",
                            "%buildingNumber%",
                            "%startDate%",
                            "%endDate%",
                        ),
                        "escapeSql": False,
                        "parameter": [
                            {
                                "name": "cityCode",
                                "defaultValue": "H224",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "citySheet",
                                "defaultValue": 3,
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "buildingNumber",
                                "defaultValue": "00006",
                                "regexpValidator": "^[\\w\\d\\s]+$",
                            },
                            {
                                "name": "startDate",
                                "defaultValue": "0001-01-01",
                            },
                            {
                                "name": "endDate",
                                "defaultValue": datetime.today().strftime(
                                    "%Y-%m-%d"
                                ),
                            },
                        ],
                    },
                }
            },
            "store": {
                "@class": "dataStore",
                "name": f"{cnf.CATASTO_OPEN_GS_WORKSPACE}:"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}",
                "href": f"{cnf.GEOSERVER_HOST}:{cnf.GEOSERVER_HOST_PORT}"
                f"/geoserver/rest"
                f"/workspaces/{cnf.CATASTO_OPEN_GS_WORKSPACE}"
                f"/datastores/"
                f"{cnf.CATASTO_OPEN_GS_DATASTORE}.json",
            },
            "serviceConfiguration": False,
            "simpleConversionEnabled": False,
            "maxFeatures": 0,
            "numDecimals": 0,
            "padWithZeros": False,
            "forcedDecimal": False,
            "overridingServiceSRS": False,
            "skipNumberMatched": False,
            "circularArcPresent": False,
            "attributes": {
                "attribute": [
                    {
                        "name": "subordinate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "property",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.Long",
                    },
                    {
                        "name": "propertytype",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "censuszone",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "category",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "_class",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "consistency",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "rent",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "lot",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.lang.String",
                    },
                    {
                        "name": "startdate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                    {
                        "name": "enddate",
                        "minOccurs": 0,
                        "maxOccurs": 1,
                        "nillable": True,
                        "binding": "java.sql.Date",
                    },
                ]
            },
        }
    },
]


def load_workspaces():
    create_workspace(workspace)


def load_data_stores():
    create_datastore(datastore)


def load_layers():
    for layer in layers:
        create_layer(layer)


def load_settings():
    settings = get_settings()
    settings["global"]["settings"]["numDecimals"] = 8
    update_settings(settings)
