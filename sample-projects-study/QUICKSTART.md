# Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Navigate to Workspace
```bash
cd /Users/damayantighosh/Documents/workspace/cursor-projects-study
```

### Step 2: Install Dependencies (Optional - Choose Project)
```bash
# Option A: Install specific project
pip install -r rest-api-data-pipeline/requirements.txt

# Option B: Install all (not recommended, use venv)
for dir in */; do
    if [ -f "$dir/requirements.txt" ]; then
        echo "Installing $dir"
        pip install -r "$dir/requirements.txt"
    fi
done
```

### Step 3: Run Tests
```bash
# Test specific project
pytest rest-api-data-pipeline/tests/ -v

# Or run all tests
pytest . -v --cov
```

---

## 📖 Choose Your Learning Path

### 🔰 I'm a Beginner
**Start here:**
1. Read: `STUDY_GUIDE.md` - Understand the overview
2. Study: `python-coding-style/README.md`
3. Run: `python python-coding-style/src/design_patterns/singleton.py`
4. Test: `pytest python-coding-style/tests/ -v`

### 👨‍💼 I Know Python, Want to Learn REST APIs
**Start here:**
1. Read: `rest-api-simple-projects/README.md`
2. Compare: Files in `without_oop/` vs `with_oop/`
3. Run: `pytest rest-api-simple-projects/tests/ -v`
4. Study: `rest-api-data-pipeline/src/api/`

### 🏗️ I Want Full-Stack Experience
**Start here:**
1. Read: `PROJECT_SUMMARY.md`
2. Study all 4 projects in order:
   - python-coding-style (foundations)
   - rest-api-simple-projects (OOP vs procedural)
   - rest-api-data-pipeline (advanced APIs)
   - kafka-producer-consumer (messaging)
3. Run all tests: `pytest . -v`

### 🚀 I Want to Extend These Projects
**Start here:**
1. Pick a project
2. Review its test file
3. Add a new feature
4. Write tests for it
5. Submit improvements

---

## 🎯 What Each Project Teaches

### `python-coding-style` (45 mins)
✓ Learn Python best practices
✓ Understand design patterns
✓ See code smells to avoid
✓ Study defensive coding
```bash
python python-coding-style/src/design_patterns/singleton.py
python python-coding-style/src/design_patterns/factory.py
```

### `rest-api-simple-projects` (1 hour)
✓ Compare OOP vs procedural
✓ Learn service layer pattern
✓ Understand dependency injection
```bash
# See the differences
diff with_oop/app.py without_oop/app.py
# Run tests
pytest tests/test_with_oop.py -v
```

### `rest-api-data-pipeline` (1.5 hours)
✓ Master REST API design
✓ Learn streaming & generators
✓ Understand stateful vs stateless
```bash
# Run API client tests
pytest tests/test_api_client.py -v
# Run data processor tests  
pytest tests/test_logging.py -v
```

### `kafka-producer-consumer` (1 hour)
✓ Learn message queue patterns
✓ Master producer-consumer
✓ Understand error handling
```bash
# Test producer functionality
pytest tests/test_kafka_producer.py -v
# Test consumer functionality
pytest tests/test_kafka_consumer.py -v
```

---

## 📚 Quick References

### Key Files by Topic

**Design Patterns:**
- Singleton: `python-coding-style/src/design_patterns/singleton.py`
- Factory: `python-coding-style/src/design_patterns/factory.py`
- Repository: `rest-api-simple-projects/with_oop/app.py` (lines 50-80)
- Service Layer: `rest-api-simple-projects/with_oop/app.py` (lines 150-200)

**Best Practices:**
- Naming: `python-coding-style/src/good_practices/naming_conventions.py`
- Type Hints: `python-coding-style/src/good_practices/type_hints.py`
- Error Handling: `python-coding-style/src/good_practices/error_handling.py`
- Defensive: `python-coding-style/src/good_practices/defensive_coding.py`

**Anti-Patterns:**
- Code Smells: `python-coding-style/src/anti_patterns/code_smells.py`

**REST APIs:**
- Stateless: `rest-api-data-pipeline/src/api/client.py` (StatelessAPIClient)
- Stateful: `rest-api-data-pipeline/src/api/client.py` (StatefulAPIClient)
- Procedural: `rest-api-simple-projects/without_oop/app.py`
- OOP: `rest-api-simple-projects/with_oop/app.py`

**Kafka:**
- Producer: `kafka-producer-consumer/src/kafka/producer.py`
- Consumer: `kafka-producer-consumer/src/kafka/consumer.py`
- Config: `kafka-producer-consumer/src/kafka/config.py`

---

## 🧪 Common Test Commands

```bash
# Run all tests
pytest . -v

# Run specific project tests
pytest rest-api-data-pipeline/tests/ -v

# Run specific test file
pytest rest-api-simple-projects/tests/test_with_oop.py -v

# Run specific test class
pytest rest-api-data-pipeline/tests/test_api_client.py::TestStatelessAPIClient -v

# Run with coverage
pytest . --cov --cov-report=html

# Run only failed tests
pytest . --lf -v

# Run tests in parallel
pytest . -n auto
```

---

## 💡 Common Tasks

### View Project Structure
```bash
# See all directories
find . -type d -maxdepth 2 | sort

# Count Python files per project
for dir in */; do
    echo "$dir: $(find "$dir" -name '*.py' | wc -l) files"
done
```

### View Key Classes
```bash
# Show all classes
grep -r "^class " --include="*.py" src/

# Show all functions
grep -r "^def " --include="*.py" src/
```

### Check Code Style
```bash
# Check with pylint (if installed)
pylint src/

# Format with black (if installed)
black src/ --check

# Type check with mypy (if installed)
mypy src/
```

### Generate Documentation
```bash
# List all modules
python -c "import pkgutil; import src; print([name for _, name, _ in pkgutil.walk_packages(src.__path__, src.__name__+'.')])"
```

---

## ❓ FAQ

**Q: I'm getting import errors**
A: Make sure you're in the project root directory and have installed dependencies:
```bash
cd /Users/damayantighosh/Documents/workspace/cursor-projects-study
pip install -r <project>/requirements.txt
```

**Q: How do I use these in my own project?**
A: Copy the relevant modules:
```bash
# Copy just the Kafka producer
cp kafka-producer-consumer/src/kafka/producer.py my_project/

# Copy API clients
cp rest-api-data-pipeline/src/api/client.py my_project/
```

**Q: Can I modify these projects?**
A: Yes! These are learning resources. Feel free to:
- Modify the code
- Add features
- Write more tests
- Create variations

**Q: How do I extend these projects?**
A: See suggestions in `PROJECT_SUMMARY.md` "Next Steps" section, or check individual README files for ideas.

**Q: Where do I find specific concepts?**
A: Use `grep` or check the file listings in `PROJECT_SUMMARY.md`.

---

## 🎓 Suggested Study Order

### Week 1: Foundations
- Day 1-2: Read `python-coding-style/README.md`
- Day 3-4: Study naming conventions and type hints
- Day 5: Learn design patterns (Singleton, Factory)
- Day 6: Study anti-patterns and code smells
- Day 7: Run all tests, review failed ones

### Week 2: API Design
- Day 8-9: Compare OOP vs procedural
- Day 10-11: Study REST API clients
- Day 12: Learn streaming and generators
- Day 13: Understand stateful vs stateless
- Day 14: Create your own API

### Week 3: Production Patterns
- Day 15: Learn service layer pattern
- Day 16: Understand dependency injection
- Day 17: Study repository pattern
- Day 18: Review all tested code
- Day 19-20: Extend one project with features
- Day 21: Review and consolidate learning

### Week 4: Messaging & Advanced
- Day 22-24: Learn Kafka producer
- Day 25-26: Learn Kafka consumer
- Day 27: Study configuration management
- Day 28: Create your own consumer/producer

---

## 🔗 Cross-References

### API Client Used By
- `rest-api-data-pipeline`: Core API client implementation
- `rest-api-simple-projects`: HTTP request handling

### Design Patterns Used In
- Singleton: Kafka config, Logger
- Factory: Database connections, UI components
- Repository: Data access layer
- Service: Business logic layer

### Logging Used In
- All projects: Error tracking and debugging
- Kafka: Message flow tracking
- API: Request/response logging

### Type Hints Used In
- All projects: IDE support, documentation
- Tests: Test data validation
- Configuration: Type-safe settings

---

## 📞 Getting Help

1. **Check the README** in the specific project
2. **Read docstrings** in the Python files
3. **Look at tests** to see usage examples
4. **Check PROJECT_SUMMARY.md** for overview
5. **Review STUDY_GUIDE.md** for concepts

---

## ✨ Quick Wins

### See Results In 5 Minutes
```bash
# 1. Run Singleton example
python python-coding-style/src/design_patterns/singleton.py

# 2. Run Factory example
python python-coding-style/src/design_patterns/factory.py

# 3. See test results
pytest python-coding-style/tests/ -v -k "test_" --tb=short
```

### Impress Yourself In 30 Minutes
```bash
# 1. Read a good_practices file
cat python-coding-style/src/good_practices/naming_conventions.py

# 2. Read corresponding anti-pattern
cat python-coding-style/src/anti_patterns/code_smells.py

# 3. See the difference in design
diff -u <(cat python-coding-style/src/anti_patterns/code_smells.py | grep "def\|class") \
        <(cat python-coding-style/src/good_practices/naming_conventions.py | grep "def\|class")

# 4. Run tests to verify
pytest python-coding-style/tests/test_good_practices.py -v
```

---

## 🎉 Ready to Start?

Pick your starting point:

**I have 15 minutes:**
→ Run tests: `pytest python-coding-style/tests/test_design_patterns.py -v`

**I have 1 hour:**
→ Study module: `python python-coding-style/src/design_patterns/singleton.py`

**I have 3 hours:**
→ Complete project: Study and test `rest-api-simple-projects`

**I have a full day:**
→ Master track: Go through all 4 projects in order

Let's get started! 🚀

