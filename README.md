# Blend_-_Share

## Bugs and Fixes

**Issue:** *ModuleNotFoundError: smoothies.forms not found.*

**Solution:** *The forms.py was accidentally saved inside templates folder. Moved forms.py into the app directory.*

---

**Issue:** *The smoothie model was missing the description field.*

**Solution:** *Added the correct line to the model.*

---

**Issue:** *'smoothies.views' had no attribute 'signup'.*

**Solution:** *Added the signup() function in views.py using UserCreationForm.*

---
