import dagster as dg 

@dg.asset(key_prefix="subsidiary_two",
          group_name="subsidiary_two",
          deps=[dg.AssetKey(["subsidiary_one", "accounts"]),
          dg.AssetKey(["subsidiary_one", "payments"])])
def accounts_receivable(context: dg.AssetExecutionContext) -> None:
    context.log.info("accounts receivable is materialized")


@dg.asset(key_prefix="subsidiary_two",
          group_name="subsidiary_two",
          )
def accounts_payable(context: dg.AssetExecutionContext) -> None:
    context.log.info("accounts payable is materialized")


@dg.asset(key_prefix="subsidiary_two",
          group_name="subsidiary_two",
          deps=[dg.AssetKey(["subsidiary_two", "accounts_payable"])])
def overdue_payments(context: dg.AssetExecutionContext) -> None:
    context.log.info("accounts payable is materialized")

@dg.asset(key_prefix="subsidiary_two",
          group_name="subsidiary_two",
          deps=[dg.AssetKey(["subsidiary_two", "overdue_payments"])])
def collection_attempts(context: dg.AssetExecutionContext) -> None:
    context.log.info("accounts payable is materialized")