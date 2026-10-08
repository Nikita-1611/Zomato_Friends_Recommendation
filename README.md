# Taste-matched picks: clickable prototype

A PM portfolio prototype for a food delivery feature: use **repeat orders**, not star ratings, as the taste signal, and show 1–3 dish picks with a one-line reason you can check. Fake data only, no backend.

Open `index.html` in a browser. On a laptop it shows a phone with a short presenter guide beside it; on a phone it fills the screen. There are no demo controls inside the app: every moment is reached through normal app actions.

## 60-second run
1. Home: tap the reason under Riya's pick → "Why this pick?"
2. Add to cart → View cart → Place order → "Order delivered"
3. Home → Order again → Reorder Ghee roast dosa → Place order. It's the user's 3rd order of that dish, so "Looks like a favourite. Recommend it to your friends?" appears → Recommend
4. Friends tab: follow Arjun, filter by person, tap Why? on any pick
5. Tap "Home ▾" and switch the address to Office: fewer than 20 people there reorder the same places, so "Highly rated nearby" (labelled as ratings) replaces the group section
6. Profile: toggle sharing, hide a shared pick

"Restart demo" sits in the presenter guide and at the bottom of Home and Profile.

## Privacy rules the prototype enforces
- No order counts, dates, times or prices next to a friend's name.
- Strangers only appear as a group, never by name.
- Group counts only show when the group is 20 people or more; below that, the ratings fallback appears and no count is shown.
- Only opted-in friends appear (the data includes a friend who hasn't opted in, and they never show).

## Files
- `prototype/template.html`: the page source (HTML, CSS, JS).
- `prototype/build.py`: embeds the images and writes `prototype/taste-matched-picks.html` and `index.html`. Run `python3 prototype/build.py` after editing the template.
- `prototype/assets/`: dish art and avatars. See `prototype/assets/CREDITS.md`.
