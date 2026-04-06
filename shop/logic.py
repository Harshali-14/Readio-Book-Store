from shop.models import Book, Category

def get_recommendation(message):
    message = message.lower()

    # 🔑 Keyword mapping
    keyword_map = {
        "Programming": ["python", "programming", "coding", "web",],
        "ai": ["ai", "machine learning", "deep learning", "AI"],
        "web": ["web", "html", "css", "javascript"],
        "Romance": ["romance", "love"],
        "Adventure": ["adventure", "action"],
        "self help": ["self help", "motivation", "success", "Self-Help"],
        "Data Structure": ["data science", "data", "analytics", "Data Structure", "dsa"],
        "business": ["business", "startup", "finance", "Bussiness"],
        "comedy": ["funny", "intresting", "Comedy"],
        "Science" : ["biology", "bio", "history", "science"],
        "Drama": ["action", "script", "drama" ],
    }

    matched_category = None

    # 🔍 Find matching category using keywords
    for category_name, keywords in keyword_map.items():
        for keyword in keywords:
            if keyword in message:
                matched_category = category_name
                break

    # 📚 If category found
    if matched_category:
        try:
            # 🔥 IMPORTANT: flexible match (case-insensitive + partial)
            category = Category.objects.filter(
                name__icontains=matched_category
            ).first()

            if not category:
                return f"❌ Category '{matched_category}' not found in database."

            books = Book.objects.filter(category=category)

            if books.exists():
                response = f"📚 Books in {category.name}:\n\n"

                for book in books:
                    response += f"- {book.title} (₹{book.price})\n"

                return response

            return f"❌ No books found in {category.name} category."

        except Exception as e:
            return "❌ Something went wrong."

    # ❌ Fallback
    return "📚 Try: Python, AI, Web, Romance, Adventure, Self Help, Data Science, Business"