Generate Code for this requirement: Jira Ticket:
User Verification System 

Labels:
- Verification
- User Management
- Admin Activity
- Unit Test 

Assignee:
Hamza Hasan

Shared Files:










Code Changes:

--- main/kotlin/com/google/samples/apps/sunflower/data/database/db/DbUser.kt.original	2021-03-30 00:15:20.000000000 +0100
+++ main/kotlin/com/google/samples/apps/sunflower/data/database/db/DbUser.kt	2021-03-30 00:20:02.728834863 +0100
@@ -46,6 +46,16 @@ @Entity(tableName = "user")
     val creationDate: Long,
     val accessDate: Long,
     val isActive: Boolean
 ): Serializable {
+    // Unhide the constructor to make it accessible from this package and any subpackages
+    constructor() : this(0, 0, "", "", "", false)
+
     @PrimaryKey
     @ColumnInfo(name = "id")
+    var id: Long? = null

     @ColumnInfo(name = "email")
     @get:Exclude
     var email: String

```



```
diff
--- a/app/src/main/kotlin/com/example/userverification/db/schema/UserSchema.kt
+++ b/app/