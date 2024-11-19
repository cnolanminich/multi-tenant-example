import dagster as dg 

@dg.asset(key_prefix="subsidiary_one",
          group_name="subsidiary_one")
def accounts(context: dg.AssetExecutionContext) -> None:
    context.log.info("accounts is materialized")

@dg.asset(key_prefix="subsidiary_one",
          group_name="subsidiary_one")
def payments(context: dg.AssetExecutionContext) -> None:
    context.log.info("payments is materialized")