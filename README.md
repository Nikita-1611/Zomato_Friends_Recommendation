# Taste-matched picks: clickable prototype

A PM portfolio prototype for a food delivery feature: dish picks based on **repeat orders, not star ratings**, from friends you choose and from groups of 20+ nearby people who reorder the same places as you. The layout follows a mainstream Indian food delivery app (home, search, restaurant menu). No logo or brand name; restaurants, people and prices are invented.

## Links
- **▶ Live prototype:** https://nikita-1611.github.io/Zomato_Friends_Recommendation/
- **Slide deck:** https://claude.ai/artifact/NEk7dT15dS5UvC1nAD6RAD (private until shared); slide sources are in `deck/`
- Backup prototype link: https://raw.githack.com/nikita-1611/Zomato_Friends_Recommendation/claude/taste-matched-picks-prototype-5lh87a/index.html

Or download `index.html` and open it in a browser. On a laptop it shows a phone; on a phone it fills the screen.

## Screens
- **Home**: address switcher, search, VEG toggle, deals carousel, membership strip, categories, filter chips, then
  - **From your friends**: picks from friends who opted in and whom you chose ("Riya keeps coming back to this")
  - **Because you love Hyderabadi dum biryani**: "42 people near you who reorder the same places as you", including one **Something new** pick
  - **Recommended for you**: 3-per-row restaurant cards
  - Floating bar: Home | Healthy | Friends | Dining
- **Friends tab**: friends' dish stories (add your own), friends' picks, **Local picks** from people who turned on a public profile (username only), and "Choose whose picks you see"
- **Search**: chips, 3 x 2 recommended grid, All restaurants > Featured cards
- **Restaurant menu**: Picks for you above Recommended for you, Highly reordered bars, ADD, Menu button, offers bar
- **Why this pick?** sheet, cart, order delivered, and the recommend prompt on the 3rd order of a dish
- **Comments**: hidden behind a small bubble icon on a few dishes. After an order, "How was it?" lets you comment on what you ordered; you can only comment on dishes you've ordered
- **Profile**: Share my favourites, Public profile, Choose whose picks you see, My shared picks with Hide

## Rules the prototype enforces
- No order counts, dates, times or prices next to a friend's name.
- Strangers are never named, only shown as a group of 20 or more, unless they turned on a public profile (then by username only).
- Friends appear only if they opted in **and** you chose them. Contacts show name + username; locals show username only.
- Local picks show only locals' comments, never friends'.
- Picks only come from restaurants that deliver to the current address (switch Home / Office to see it).
- Every pick has **Not for me**.

## Demo controls (bottom of Home)
- **Restart demo**
- **Simulate quiet area**: group under 20, so "Highly rated nearby (based on ratings)" replaces the group section
- **Simulate 3rd reorder**: places a 3rd order of Hyderabadi dum biryani and shows the recommend prompt
- **Simulate new user (0 orders)**: hides personal picks, shows "Highly reordered near you" and 3 quick taps, then 2 picks "Based on your answers"

## Photos
23 dishes have real photos in `prototype/assets/photos/<dish id>.jpg`; the rest show a plain stand-in tile. Sources and licences are listed in `prototype/assets/photos/CREDITS.md` and still need confirming before wide sharing. After adding a photo, run `python3 prototype/build.py`.

## Deploying
Every push to this branch republishes the site to GitHub Pages (`.github/workflows/deploy.yml`), live in about a minute.

## Files
- `prototype/template.html`: page source
- `prototype/build.py`: embeds photos, writes `prototype/taste-matched-picks.html` and `index.html`
- `deck/`: slide deck sources (one HTML file per slide, order in `deck.json`)
