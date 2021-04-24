from CSMCBudgeting.CSMCApp.membership import Membership
from CSMCBudgeting.CSMCApp.subs import Subscriptions
from CSMCBudgeting.model.model import Members
from config import Config

member_object = Membership(Config, Members)

# Adds Member
# member_object.add_new_member("Madara Dziedataja", "2021-04-18")

# Updates Member
# member_object.update_existing_member("Madara Dziedataja", "dateLeft", "2021-04-24")

# Deletes all data (cant be undone)
# member_object.delete_row("Madara Dziedataja")

# Queries all Members
result_set = member_object.query_all_members()
print(result_set)

# Subscriptions
subscriptions = Subscriptions(Config, result_set)
new_subs = subscriptions.generate_subs_for_active_members()
subscriptions.commit_new_subs_to_database(new_subs)
print(new_subs)
