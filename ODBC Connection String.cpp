#include <iostream>
#include <windows.h>
#include <sqlext.h>

// Example ODBC Connection String
#define CONNECTION_STRING "Driver={SQL Server};Server=myServer123.database.windows.net;Database=myDatabase123;Uid=myUser123;Pwd=mySuperSecretPassword!;"

void connect_to_database() {
    SQLHENV henv; // Environment handle
    SQLHDBC hdbc; // Connection handle
    SQLRETURN retcode;

    // Allocate environment handle
    retcode = SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &henv);

    // Set the ODBC version environment attribute
    if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
        retcode = SQLSetEnvAttr(henv, SQL_ATTR_ODBC_VERSION, (SQLPOINTER)SQL_OV_ODBC3, 0);
        
        // Allocate connection handle
        if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
            retcode = SQLAllocHandle(SQL_HANDLE_DBC, henv, &hdbc);

            // Connect to the database
            retcode = SQLDriverConnect(hdbc, NULL, (SQLCHAR*)CONNECTION_STRING, SQL_NTS, NULL, 0, NULL, SQL_DRIVER_NOPROMPT);

            if (retcode == SQL_SUCCESS || retcode == SQL_SUCCESS_WITH_INFO) {
                std::cout << "Connected to database successfully." << std::endl;
                // Perform database operations here
            } else {
                std::cerr << "Failed to connect to database." << std::endl;
            }

            // Disconnect and free the connection handle
            SQLDisconnect(hdbc);
            SQLFreeHandle(SQL_HANDLE_DBC, hdbc);
        } else {
            std::cerr << "Failed to allocate connection handle." << std::endl;
        }

        // Free the environment handle
        SQLFreeHandle(SQL_HANDLE_ENV, henv);
    } else {
        std::cerr << "Failed to allocate environment handle." << std::endl;
    }
}

int main() {
    connect_to_database();
    return 0;
}
