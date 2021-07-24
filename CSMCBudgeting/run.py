from CSMCBudgeting.CSMCApp.membership import Membership
from CSMCBudgeting.CSMCApp.model import Members, Remittance
from CSMCBudgeting.CSMCApp.subs import OutstandingDebts, DebtManager
from config import Config

member_object = Membership(Config, Members)

# Adds Member
# member_object.add_new_member("Scott Haaden", "2021-04-18")

# Updates Member
# member_object.update_existing_member("Alex Neville", "dateLeft", None)

# Deletes all data (cant be undone)
# member_object.delete_row("Scott Haden")

# Queries all Members
# result_set = member_object.query_all_members()
# print(result_set)


# Subscriptions

# subscriptions = MonthlySubscriptions(Config, result_set)
# new_subs = subscriptions.generate_subs_for_active_members()
# subscriptions.commit_new_subs_to_database(new_subs)
# print(new_subs)

# Active remittance
remittanceobject = OutstandingDebts(Config, "foo", "bar")
unpaid = remittanceobject.get_all_unpaid_remittance()
print(unpaid)
wookie_data = DebtManager(unpaid, Config, Remittance, "Wookie")

print(wookie_data.summarize_outstanding_payments())
fun = wookie_data.pay_remittance(category="subs", date="2021-06-01")
# vern_fun = vern_data.pay_remittance(category="subs")
# print(vern_fun)
