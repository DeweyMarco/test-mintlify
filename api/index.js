const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const quotes = [
  { id: "1", text: "The only way to do great work is to love what you do.", author: "Steve Jobs", category: "motivation" },
  { id: "2", text: "In the middle of every difficulty lies opportunity.", author: "Albert Einstein", category: "motivation" },
  { id: "3", text: "It does not matter how slowly you go as long as you do not stop.", author: "Confucius", category: "motivation" },
  { id: "4", text: "The unexamined life is not worth living.", author: "Socrates", category: "philosophy" },
  { id: "5", text: "I think, therefore I am.", author: "René Descartes", category: "philosophy" },
  { id: "6", text: "The only true wisdom is in knowing you know nothing.", author: "Socrates", category: "wisdom" },
  { id: "7", text: "Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself.", author: "Rumi", category: "wisdom" },
  { id: "8", text: "In three words I can sum up everything I've learned about life: it goes on.", author: "Robert Frost", category: "wisdom" },
  { id: "9", text: "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.", author: "Albert Einstein", category: "humor" },
  { id: "10", text: "I have not failed. I've just found 10,000 ways that won't work.", author: "Thomas Edison", category: "humor" },
  { id: "11", text: "The computer was born to solve problems that did not exist before.", author: "Bill Gates", category: "technology" },
  { id: "12", text: "Any sufficiently advanced technology is indistinguishable from magic.", author: "Arthur C. Clarke", category: "technology" },
  { id: "13", text: "The advance of technology is based on making it fit in so that you don't really even notice it.", author: "Bill Gates", category: "technology" },
  { id: "14", text: "Simplicity is the ultimate sophistication.", author: "Leonardo da Vinci", category: "wisdom" },
  { id: "15", text: "Be yourself; everyone else is already taken.", author: "Oscar Wilde", category: "humor" },
];

const VALID_CATEGORIES = [...new Set(quotes.map((q) => q.category))].sort();

app.get("/categories", (req, res) => {
  res.json({ categories: VALID_CATEGORIES });
});

app.get("/quotes/random", (req, res) => {
  const { category } = req.query;
  if (category && !VALID_CATEGORIES.includes(category)) {
    return res.status(400).json({
      error: "invalid_category",
      message: `Category '${category}' does not exist. Valid categories: ${VALID_CATEGORIES.join(", ")}`,
    });
  }
  const pool = category ? quotes.filter((q) => q.category === category) : quotes;
  res.json(pool[Math.floor(Math.random() * pool.length)]);
});

app.get("/quotes", (req, res) => {
  const { category, limit } = req.query;
  if (category && !VALID_CATEGORIES.includes(category)) {
    return res.status(400).json({
      error: "invalid_category",
      message: `Category '${category}' does not exist. Valid categories: ${VALID_CATEGORIES.join(", ")}`,
    });
  }
  let results = category ? quotes.filter((q) => q.category === category) : quotes;
  if (limit !== undefined) {
    const n = parseInt(limit, 10);
    if (isNaN(n) || n < 1) {
      return res.status(400).json({ error: "invalid_limit", message: "limit must be a positive integer" });
    }
    results = results.slice(0, n);
  }
  res.json({ quotes: results, total: results.length });
});

app.get("/quotes/:id", (req, res) => {
  const quote = quotes.find((q) => q.id === req.params.id);
  if (!quote) {
    return res.status(404).json({
      error: "not_found",
      message: `No quote found with id '${req.params.id}'`,
    });
  }
  res.json(quote);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Quotes API running on http://localhost:${PORT}`));
