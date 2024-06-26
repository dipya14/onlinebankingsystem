from django.contrib import admin
from .models import Profile, Branch, Account, Transaction

admin.site.register(Profile)
admin.site.register(Branch)

class AccountAdmin(admin.ModelAdmin):
	list_display = ('account_number', 'user', 'branch_name', 'account_holder_name', 'balance', 'opened_date', 'is_active')
	readonly_fields = ('account_holder_name', 'account_number', 'opened_date', 'ifsc')

	def save_model(self, request, obj, form, change):
		obj.account_holder_name = f"{obj.user.profile.user.first_name} {obj.user.profile.user.last_name}"

		if obj.pk is None:
			if obj.branch_name:  # Check if branch_name is not None
				obj.ifsc = obj.branch_name.ifsc  # Assign the ifsc from the associated branch

				# Generate the account number
				last_six_digits_of_ifsc = obj.ifsc[-6:]
				account_numbers = Account.objects.filter(branch_name=obj.branch_name)
				next_account_number = str(account_numbers.count() + 1).zfill(6)
				obj.account_number = f"{last_six_digits_of_ifsc}{next_account_number}"

		super().save_model(request, obj, form, change)

admin.site.register(Account, AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['bank_reference_no', 'amount', 'timestamp', 'sender_account', 'receiver_account_number', 'receiver_ifsc']

admin.site.register(Transaction, TransactionAdmin)