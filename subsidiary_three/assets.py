import dagster as dg 

@dg.asset(key_prefix="subsidiary_three",
          group_name="subsidiary_three",
          )
def another_asset(context: dg.AssetExecutionContext) -> None:
    context.log.info("another asset is materialized")


@dg.asset(key_prefix="subsidiary_three",
          group_name="subsidiary_three",
          deps=[dg.AssetKey(["subsidiary_three", "another_asset"])]
          )
def downstream_asset(context: dg.AssetExecutionContext) -> None:
    context.log.info("downstream asset is materialized")
