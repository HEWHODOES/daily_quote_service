# Daily Philosophy Quotes

Daily philosophical quotes delivered via email - a simple service to brighten your day.

## Features
- User selects philosophy category (Stoicism, Epicureanism, etc.)
- Flexible time windows (fixed time or time range for surprise delivery)
- Smart rotation: No duplicates, quotes repeat after 60 days
- Spam protection: Email confirmation required for registration
- Subscription management: Pause, change settings, delete account
- Clean email design: Beautiful layout with quote centered

## Tech Stack
- Python + Flask
- SQLite3
- JS + CSS
- SendGrid (email delivery)
- APScheduler (automatic sending every 15 minutes)
- Hosting: Render.com

## Database Structure
- **tbl_users**: User accounts with soft delete
- **tbl_user_preferences**: Philosophy choices + time windows
- **tbl_quote_history**: Tracks sent quotes (prevents duplicates)
- **tbl_quotes**: The quotes themselves
- **tbl_categories**: Philosophy categories
- **tbl_quote_categories**: Many-to-many junction table

## Status
🚧 Planning complete - DB schema + flows finalized, ready for implementation

## Development Roadmap
1. ✅ Planning + DB design
2. ⏳ Initialize DB + console tools for management
3. ⏳ APScheduler test (email sending logic)
4. ⏳ Login/registration + subscription logic
5. ⏳ Main site (user dashboard)
6. ⏳ Landing page + login UI