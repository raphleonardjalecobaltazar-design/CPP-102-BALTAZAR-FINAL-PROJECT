# Test Cases – Student Grade Monitoring System

**Tested by:** Raph Leonard J. Baltazar  
**Date:** October 14, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Displays the five initial grades: 97, 69, 67, 65, 87. | Displays all five grades correctly. | Pass |
| TC02 | Choose 2, enter 33 | Grade added successfully! | Grade 33 is added successfully. | Pass |
| TC03 | Choose 2, enter abc | Invalid input. Please enter a valid character. | Displays the invalid input message. | Pass |
| TC04 | Choose 2, enter 101 | Invalid grade. Enter a value from 0 to 100. | Displays the invalid grade message. | Pass |
| TC05 | Choose 3 | Classifies grades of 90 and above as EXCELLENT, 75–89 as PASSED, and below 75 as FAILED. | Correctly classifies the initial grades. | Pass |
| TC06 | Choose 4 | Displays the grade count, total, average, lowest grade, highest grade, percentages, and overall status. | Displays the summary for the initial grades. | Pass |
| TC07 | Choose 6 | Invalid choice. Please try again. | Displays the invalid choice message. | Pass |
| TC08 | Choose 2, enter 0 | Grade added successfully! | Grade 0 is added successfully. | Pass |
| TC09 | Choose 2, enter 100 | Grade added successfully! | Grade 100 is added successfully. | Pass |
| TC10 | Choose 5 | Thank you for using the Student Grade Monitoring System. The program terminates. | Displays the exit message and stops the program. | Pass |

## Bugs Found and Fixed

- **Hardest test:** TC04 — entering a grade of 101 or beyond.
- **Explanation:** The program must reject grades outside the range of 0–100.
- **Result:** The existing validation correctly rejects the invalid grade, so no code modification is required.
