from django.db import models

# Model to represent properties
class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

# Model to represent tenants within a property
class Tenant(models.Model):
    property = models.ForeignKey(Property, related_name='tenants', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    iban = models.CharField(max_length=34)

    def __str__(self):
        return f"{self.name} ({self.property.name})"

# Model to represent expense categories
class ExpenseProfile(models.Model):
    UST_CHOICES = [(0, '0%'),(7, '7%'), (19, '19%')]
    UST_SCH_CHOICES = [('Nicht', 'Nicht'), ('Voll', 'Voll'), ('Teilw', 'Teilw')]

    profile_name = models.CharField(max_length=255, unique=True)  # Profile Name for categorization
    account_name = models.CharField(max_length=255, unique=True)  # Account Name for matching with ParsedTransaction
    ust = models.IntegerField(choices=UST_CHOICES, default=19)  # UST Dropdown
    ust_sch = models.CharField(max_length=10, choices=UST_SCH_CHOICES, default='Voll')  # UST-Sch Dropdown
    transactions = models.ManyToManyField('ParsedTransaction', related_name='expense_profiles', blank=True)

    def __str__(self):
        return self.profile_name

# Model to represent parsed transactions after categorization
class ParsedTransaction(models.Model):
    date = models.DateField()
    account_name = models.CharField(max_length=255, null=True, blank=True)  # New field for account name
    gggkto = models.ForeignKey('ExpenseProfile', null=True, blank=True, on_delete=models.SET_NULL)
    betrag_brutto = models.FloatField(null=True, blank=True)  # Original amount

    def __str__(self):
        return f"{self.date} | {self.account_name} | {self.betrag_brutto} | {self.gggkto}"

    @property
    def ust(self):
        """Calculate UST dynamically based on the linked ExpenseProfile."""
        if self.gggkto:
            ust_rate = float(self.gggkto.ust) / 100
            return round(self.betrag_brutto * ust_rate, 2)
        return 0.0

    @property
    def betrag_netto(self):
        """Calculate Betrag Netto dynamically based on the linked ExpenseProfile."""
        return round(self.betrag_brutto - self.ust, 2)


# Model to represent transactions that are not yet categorized
class EarmarkedTransaction(models.Model):
    date = models.CharField(max_length=10)  # Keep DD.MM.YYYY format as a string
    amount = models.FloatField()    
    description = models.TextField()
    is_income = models.BooleanField()
    account_name = models.CharField(max_length=255, null=True, blank=True)  # New field for account name

    def __str__(self):
        return f"Earmarked {self.amount} on {self.date}"

