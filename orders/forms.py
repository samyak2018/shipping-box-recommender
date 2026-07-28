from django import forms

from .models import Product


class OrderCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for product in Product.objects.all():
            self.fields[f"product_{product.id}"] = forms.IntegerField(
                label=product.name,
                min_value=0,
                initial=0,
                required=False,
            )

    def clean(self):
        cleaned_data = super().clean()

        has_product = any(
            quantity and quantity > 0
            for quantity in cleaned_data.values()
        )

        if not has_product:
            raise forms.ValidationError(
                "Please select at least one product."
            )

        return cleaned_data