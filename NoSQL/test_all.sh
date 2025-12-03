#!/bin/bash
# Comprehensive test script for NoSQL project

echo "=========================================="
echo "NoSQL Project - Comprehensive Test Suite"
echo "=========================================="
echo ""

# Set MongoDB path
export PATH="/opt/homebrew/opt/mongodb-community@4.4/bin:$PATH"

# Check MongoDB is running
echo "1. Checking MongoDB status..."
if pgrep -x "mongod" > /dev/null; then
    echo "✅ MongoDB is running"
else
    echo "❌ MongoDB is not running. Starting it..."
    brew services start mongodb/brew/mongodb-community@4.4
    sleep 2
fi
echo ""

# Test MongoDB Shell Scripts
echo "2. Testing MongoDB Shell Scripts..."
echo ""

echo "Task 0: List databases"
mongo < 0-list_databases 2>/dev/null | grep -E "(admin|config|local)" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Task 0: PASS"
else
    echo "❌ Task 0: FAIL"
fi

echo "Task 2: Insert document"
cat 2-insert | mongo my_db 2>/dev/null | grep "nInserted" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Task 2: PASS"
else
    echo "❌ Task 2: FAIL"
fi

echo "Task 3: List all documents"
cat 3-all | mongo my_db 2>/dev/null | grep "Holberton school" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Task 3: PASS"
else
    echo "❌ Task 3: FAIL"
fi

echo "Task 4: Match documents"
cat 4-match | mongo my_db 2>/dev/null | grep "Holberton school" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Task 4: PASS"
else
    echo "❌ Task 4: FAIL"
fi

echo "Task 5: Count documents"
count=$(cat 5-count | mongo my_db 2>/dev/null | grep -E "^[0-9]+$")
if [ -n "$count" ]; then
    echo "✅ Task 5: PASS (Count: $count)"
else
    echo "❌ Task 5: FAIL"
fi

echo "Task 6: Update documents"
cat 6-update | mongo my_db 2>/dev/null | grep "nModified" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ Task 6: PASS"
else
    echo "❌ Task 6: FAIL"
fi

echo ""

# Test Python Scripts
echo "3. Testing Python Scripts..."
echo ""

echo "Task 8: List all documents (Python)"
./8-main.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Task 8: PASS"
else
    echo "❌ Task 8: FAIL"
fi

echo "Task 9: Insert school (Python)"
./9-main.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Task 9: PASS"
else
    echo "❌ Task 9: FAIL"
fi

echo "Task 10: Update topics (Python)"
./10-main.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Task 10: PASS"
else
    echo "❌ Task 10: FAIL"
fi

echo "Task 11: Schools by topic (Python)"
./11-main.py > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✅ Task 11: PASS"
else
    echo "❌ Task 11: FAIL"
fi

echo "Task 12: Log stats (Python)"
./populate_nginx_logs.py > /dev/null 2>&1
output=$(./12-log_stats.py 2>/dev/null | grep "logs")
if [ -n "$output" ]; then
    echo "✅ Task 12: PASS"
else
    echo "❌ Task 12: FAIL"
fi

echo ""

# Check documentation
echo "4. Checking Documentation..."
echo ""

echo "Checking module documentation..."
doc=$(python3 -c 'print(__import__("8-all").__doc__)' 2>/dev/null)
if [ -n "$doc" ]; then
    echo "✅ Module docs: PASS"
else
    echo "❌ Module docs: FAIL"
fi

echo "Checking function documentation..."
doc=$(python3 -c 'print(__import__("8-all").list_all.__doc__)' 2>/dev/null)
if [ -n "$doc" ]; then
    echo "✅ Function docs: PASS"
else
    echo "❌ Function docs: FAIL"
fi

echo ""

# Check file requirements
echo "5. Checking File Requirements..."
echo ""

echo "Checking Python shebangs..."
shebang_ok=true
for file in *.py; do
    if [ -f "$file" ] && [ "$file" != "populate_nginx_logs.py" ]; then
        first_line=$(head -n 1 "$file")
        if [[ "$first_line" != "#!/usr/bin/env python3" ]]; then
            echo "❌ $file: Missing or incorrect shebang"
            shebang_ok=false
        fi
    fi
done
if [ "$shebang_ok" = true ]; then
    echo "✅ Shebangs: PASS"
fi

echo "Checking MongoDB script comments..."
comment_ok=true
for file in 0-list_databases 2-insert 3-all 4-match 5-count 6-update 7-delete; do
    if [ -f "$file" ]; then
        first_line=$(head -n 1 "$file")
        if [[ "$first_line" != //* ]]; then
            echo "❌ $file: Missing comment"
            comment_ok=false
        fi
    fi
done
if [ "$comment_ok" = true ]; then
    echo "✅ MongoDB script comments: PASS"
fi

echo "Checking file permissions..."
perm_ok=true
for file in *.py; do
    if [ -f "$file" ] && [ ! -x "$file" ]; then
        echo "❌ $file: Not executable"
        perm_ok=false
    fi
done
if [ "$perm_ok" = true ]; then
    echo "✅ File permissions: PASS"
fi

echo ""
echo "=========================================="
echo "Test Suite Complete!"
echo "=========================================="
echo ""
echo "📚 Documentation Files:"
echo "   - README.md (Project requirements)"
echo "   - QUICK_START.md (NoSQL comprehensive guide)"
echo "   - PROJECT_SUMMARY.md (Setup and quick reference)"
echo "   - TASKS_OVERVIEW.md (Detailed task breakdown)"
echo ""
echo "🎉 Your NoSQL project is ready!"

