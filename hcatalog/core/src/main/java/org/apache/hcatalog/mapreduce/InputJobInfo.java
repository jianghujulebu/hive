/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.hcatalog.mapreduce;

import java.io.Serializable;
import java.util.List;
import java.util.Properties;

import org.apache.hadoop.hive.common.classification.InterfaceAudience;
import org.apache.hadoop.hive.common.classification.InterfaceStability;
import org.apache.hadoop.hive.metastore.MetaStoreUtils;

/**
 * Container for metadata read from the metadata server.
 * Prior to release 0.5, InputJobInfo was a key part of the public API, exposed directly
 * to end-users as an argument to
 * {@link HCatInputFormat#setInput(org.apache.hadoop.mapreduce.Job, InputJobInfo)}.
 * Going forward, we plan on treating InputJobInfo as an implementation detail and no longer
 * expose to end-users. Should you have a need to use InputJobInfo outside HCatalog itself,
 * please contact the developer mailing list before depending on this class.
 */
@InterfaceAudience.Private
@InterfaceStability.Evolving
public class InputJobInfo implements Serializable {

    /** The serialization version */
    private static final long serialVersionUID = 1L;

    /** The db and table names. */
    private final String databaseName;
    private final String tableName;

    /** meta information of the table to be read from */
    private HCatTableInfo tableInfo;

    /** The partition filter */
    private final String filter;

    /** The list of partitions matching the filter. */
    private List<PartInfo> partitions;

    /** implementation specific job properties */
    private final Properties properties;

    /**
     * Initializes a new InputJobInfo
     * for reading data from a table.
     * @param databaseName the db name
     * @param tableName the table name
     * @param filter the partition filter
     * @param properties implementation specific job properties
     */
    public static InputJobInfo create(String databaseName,
                                      String tableName,
                                      String filter,
                                      Properties properties) {
        return new InputJobInfo(databaseName, tableName, filter, properties);
    }

    /**
     * Initializes a new InputJobInfo
     * for reading data from a table.
     * @param databaseName the db name
     * @param tableName the table name
     * @param filter the partition filter
     */
    @Deprecated
    public static InputJobInfo create(String databaseName,
                                      String tableName,
                                      String filter) {
        return create(databaseName, tableName, filter, null);
    }


    private InputJobInfo(String databaseName,
                         String tableName,
                         String filter,
                         Properties properties) {
        this.databaseName = (databaseName == null) ?
            MetaStoreUtils.DEFAULT_DATABASE_NAME : databaseName;
        this.tableName = tableName;
        this.filter = filter;
        this.properties = properties == null ? new Properties() : properties;
    }

    /**
     * Gets the value of databaseName
     * @return the databaseName
     */
    public String getDatabaseName() {
        return databaseName;
    }

    /**
     * Gets the value of tableName
     * @return the tableName
     */
    public String getTableName() {
        return tableName;
    }

    /**
     * Gets the table's meta information
     * @return the HCatTableInfo
     */
    public HCatTableInfo getTableInfo() {
        return tableInfo;
    }

    /**
     * set the tablInfo instance
     * this should be the same instance
     * determined by this object's DatabaseName and TableName
     * @param tableInfo
     */
    void setTableInfo(HCatTableInfo tableInfo) {
        this.tableInfo = tableInfo;
    }

    /**
     * Gets the value of partition filter
     * @return the filter string
     */
    public String getFilter() {
        return filter;
    }

    /**
     * @return partition info
     */
    public List<PartInfo> getPartitions() {
        return partitions;
    }

    /**
     * @return partition info  list
     */
    void setPartitions(List<PartInfo> partitions) {
        this.partitions = partitions;
    }

    /**
     * Set/Get Property information to be passed down to *StorageHandler implementation
     * put implementation specific storage handler configurations here
     * @return the implementation specific job properties
     */
    public Properties getProperties() {
        return properties;
    }
}
