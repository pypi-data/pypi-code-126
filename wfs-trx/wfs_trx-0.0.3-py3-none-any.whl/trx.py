from typing import List, Tuple

import wfs_trx.schema_builder as builder



def insert_point(*,
    namespaces: List[dict],
    featureType: str,
    props: List[dict],
    point: Tuple[float, float],
    srs: int = 3857
) -> str:
    return builder.trx(
        namespaces,
        builder.insert(
            featureType,
            f"""
            {builder.props(props)}
            {builder.geom(builder.point(point, srs))}
            """))


def update(*,
    fid: str,
    namespaces: List[dict],
    typeName: str,
    props: List[dict]
) -> str:
    return builder.trx(
        namespaces,
        builder.update(typeName,
            f"""{' '.join([builder.property(prop['key'], prop['val']) for prop in props])}{builder.filter(fid)}"""))


def delete(*,
    fid: str,
    namespaces: List[dict],
    typeName: str
) -> str:
    return builder.trx(
        namespaces,
        builder.delete(typeName,
            builder.filter(fid)))
            

def get_container(
    namespaces: List[dict],
    typeName: str,
    geom_prop: str,
    point: Tuple[float, float],  
):
    return builder.get_feature(
        namespaces=namespaces,
        value=builder.query(
            typeName=typeName,
            value=builder.filter(
                value=builder.contains(
                    geom_prop=geom_prop,
                    geom=builder.point(coordinates=point, srs=3857)
                )
            )
        )
    )