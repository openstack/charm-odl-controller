# Copyright 2016 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# flake8: noqa
ODL_023_FEATURE_LIST = """
client: JAVA_HOME not set; results may vary
Name                                  | Version             | Installed | Repository                               | Description                                       
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
odl-aaa-all                           | 0.1.3-Helium-SR3    |           | odl-aaa-0.1.3-Helium-SR3                 | OpenDaylight :: AAA :: Authentication :: All Featu
odl-aaa-authn                         | 0.1.3-Helium-SR3    | x         | odl-aaa-0.1.3-Helium-SR3                 | OpenDaylight :: AAA :: Authentication             
odl-aaa-authn-sssd                    | 0.1.3-Helium-SR3    |           | odl-aaa-0.1.3-Helium-SR3                 | OpenDaylight :: AAA :: SSSD Federation            
odl-aaa-authn-plugin                  | 0.1.3-Helium-SR3    |           | odl-aaa-0.1.3-Helium-SR3                 | OpenDaylight :: AAA :: ODL NETCONF Plugin         
framework-security                    | 3.0.1               |           | standard-3.0.1                           | OSGi Security for Karaf                           
standard                              | 3.0.1               | x         | standard-3.0.1                           | Karaf standard feature                            
aries-annotation                      | 3.0.1               |           | standard-3.0.1                           | Aries Annotations                                 
wrapper                               | 3.0.1               |           | standard-3.0.1                           | Provide OS integration                            
service-wrapper                       | 3.0.1               |           | standard-3.0.1                           | Provide OS integration (alias to wrapper feature) 
obr                                   | 3.0.1               |           | standard-3.0.1                           | Provide OSGi Bundle Repository (OBR) support      
config                                | 3.0.1               | x         | standard-3.0.1                           | Provide OSGi ConfigAdmin support                  
region                                | 3.0.1               |           | standard-3.0.1                           | Provide Region Support                            
package                               | 3.0.1               | x         | standard-3.0.1                           | Package commands and mbeans                       
http                                  | 3.0.1               | x         | standard-3.0.1                           | Implementation of the OSGI HTTP Service           
http-whiteboard                       | 3.0.1               |           | standard-3.0.1                           | Provide HTTP Whiteboard pattern support           
war                                   | 3.0.1               | x         | standard-3.0.1                           | Turn Karaf as a full WebContainer                 
jetty                                 | 8.1.9.v20130131     |           | standard-3.0.1                           |                                                   
kar                                   | 3.0.1               | x         | standard-3.0.1                           | Provide KAR (KARaf archive) support               
webconsole                            | 3.0.1               |           | standard-3.0.1                           | Base support of the Karaf WebConsole              
ssh                                   | 3.0.1               | x         | standard-3.0.1                           | Provide a SSHd server on Karaf                    
management                            | 3.0.1               | x         | standard-3.0.1                           | Provide a JMX MBeanServer and a set of MBeans in K
scheduler                             | 3.0.1               |           | standard-3.0.1                           | Provide a scheduler service in Karaf to fire event
eventadmin                            | 3.0.1               |           | standard-3.0.1                           | OSGi Event Admin service specification for event-b
jasypt-encryption                     | 3.0.1               |           | standard-3.0.1                           | Advanced encryption support for Karaf security    
scr                                   | 3.0.1               |           | standard-3.0.1                           | Declarative Service support                       
blueprint-web                         | 3.0.1               |           | standard-3.0.1                           | Provides an OSGI-aware Servlet ContextListener for
odl-l2switch-all                      | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: All                   
odl-l2switch-switch                   | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: Switch                
odl-l2switch-switch-rest              | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: Switch                
odl-l2switch-switch-ui                | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: Switch                
odl-l2switch-hosttracker              | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: HostTracker           
odl-l2switch-addresstracker           | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: AddressTracker        
odl-l2switch-arphandler               | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: ArpHandler            
odl-l2switch-loopremover              | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: LoopRemover           
odl-l2switch-packethandler            | 0.1.3-Helium-SR3    |           | l2switch-0.1.3-Helium-SR3                | OpenDaylight :: L2Switch :: PacketHandler         
odl-packetcable-all                   | 1.1.3-Helium-SR3    |           | odl-packetcable-1.1.3-Helium-SR3         | OpenDaylight :: packetcable :: All                
odl-packetcable-consumer              | 1.1.3-Helium-SR3    |           | odl-packetcable-1.1.3-Helium-SR3         | OpenDaylight :: packetcable :: Consumer           
odl-packetcable-model                 | 1.1.3-Helium-SR3    |           | odl-packetcable-1.1.3-Helium-SR3         | OpenDaylight :: packetcable :: Model              
odl-packetcable-provider              | 1.1.3-Helium-SR3    |           | odl-packetcable-1.1.3-Helium-SR3         | OpenDaylight :: packetcable :: Provider           
odl-packetcable-driver                | 1.1.3-Helium-SR3    |           | odl-packetcable-1.1.3-Helium-SR3         | OpenDaylight :: packetcable :: Driver             
odl-netconf-connector-all             | 1.1.3-Helium-SR3    |           | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: Netconf Connector :: All          
odl-netconf-connector                 | 1.1.3-Helium-SR3    |           | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: Netconf Connector :: Netconf Conne
odl-netconf-connector-ssh             | 1.1.3-Helium-SR3    |           | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: Netconf Connector :: Netconf Conne
odl-netconf-ssh                       | 0.2.8-Helium-SR3    |           | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: Netconf Connector :: SSH          
odl-netconf-tcp                       | 0.2.8-Helium-SR3    |           | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: Netconf Connector :: TCP          
odl-snmp4sdn-all                      | 0.1.6-Helium-SR3    |           | odl-snmp4sdn-0.1.6-Helium-SR3            | OpenDaylight :: SNMP4SDN :: All                   
odl-snmp4sdn-snmp4sdn                 | 0.1.6-Helium-SR3    |           | odl-snmp4sdn-0.1.6-Helium-SR3            | OpenDaylight :: SNMP4SDN :: Plugin                
odl-plugin2oc                         | 0.1.3-Helium-SR3    |           | odl-plugin2oc-0.1.3-Helium-SR3           | OpenDaylight :: plugin2oc :: Plugin               
odl-config-all                        | 0.2.8-Helium-SR3    |           | odl-config-0.2.8-Helium-SR3              | OpenDaylight :: Config :: All                     
odl-mdsal-common                      | 1.1.3-Helium-SR3    | x         | odl-config-0.2.8-Helium-SR3              | OpenDaylight :: Config :: All                     
odl-config-api                        | 0.2.8-Helium-SR3    | x         | odl-config-0.2.8-Helium-SR3              | OpenDaylight :: Config :: API                     
odl-config-netty-config-api           | 0.2.8-Helium-SR3    | x         | odl-config-0.2.8-Helium-SR3              | OpenDaylight :: Config :: Netty Config API        
odl-config-core                       | 0.2.8-Helium-SR3    | x         | odl-config-0.2.8-Helium-SR3              | OpenDaylight :: Config :: Core                    
odl-config-manager                    | 0.2.8-Helium-SR3    | x         | odl-config-0.2.8-Helium-SR3              | OpenDaylight :: Config :: Manager                 
odl-adsal-all                         | 0.8.4-Helium-SR3    | x         | adsal-0.8.4-Helium-SR3                   | OpenDaylight AD-SAL All Features                  
odl-adsal-core                        | 0.8.4-Helium-SR3    | x         | adsal-0.8.4-Helium-SR3                   | OpenDaylight :: AD-SAL :: Core                    
odl-adsal-networkconfiguration        | 0.0.6-Helium-SR3    | x         | adsal-0.8.4-Helium-SR3                   | OpenDaylight :: AD-SAL :: Network Configuration   
odl-adsal-connection                  | 0.1.5-Helium-SR3    | x         | adsal-0.8.4-Helium-SR3                   | OpenDaylight :: AD-SAL :: Connection              
odl-adsal-clustering                  | 0.5.4-Helium-SR3    | x         | adsal-0.8.4-Helium-SR3                   | OpenDaylight :: AD-SAL :: Clustering              
odl-adsal-configuration               | 0.4.6-Helium-SR3    | x         | adsal-0.8.4-Helium-SR3                   | OpenDaylight :: AD-SAL :: Configuration           
odl-adsal-thirdparty                  | 0.8.4-Helium-SR3    | x         | adsal-0.8.4-Helium-SR3                   | OpenDaylight :: AD-SAL :: Third-Party Depenencies 
odl-config-netty                      | 0.2.8-Helium-SR3    | x         | odl-config-persister-0.2.8-Helium-SR3    | OpenDaylight :: Config-Netty                      
odl-base-all                          | 1.4.5-Helium-SR3    | x         | odl-base-1.4.5-Helium-SR3                | OpenDaylight Controller                           
odl-base-dummy-console                | 1.1.3-Helium-SR3    | x         | odl-base-1.4.5-Helium-SR3                | Temporary Dummy Console                           
odl-base-felix-dm                     | 3.1.0               | x         | odl-base-1.4.5-Helium-SR3                | Felix Dependency Manager                          
odl-base-aries-spi-fly                | 1.0.0               | x         | odl-base-1.4.5-Helium-SR3                | Aries SPI Fly                                     
odl-base-netty                        | 4.0.23.Final        | x         | odl-base-1.4.5-Helium-SR3                |                                                   
odl-base-jersey                       | 1.17                | x         | odl-base-1.4.5-Helium-SR3                | Jersey                                            
odl-base-jersey2-osgi                 | 4.0                 |           | odl-base-1.4.5-Helium-SR3                | OSGi friendly Jersey                              
odl-base-jackson                      | 2.3.2               | x         | odl-base-1.4.5-Helium-SR3                | Jackson JAX-RS                                    
odl-base-slf4j                        | 1.7.2               | x         | odl-base-1.4.5-Helium-SR3                | SLF4J Logging                                     
odl-base-apache-commons               | 1.4.5-Helium-SR3    | x         | odl-base-1.4.5-Helium-SR3                | Apache Commons Libraries                          
odl-base-eclipselink-persistence      | 2.0.4.v201112161009 | x         | odl-base-1.4.5-Helium-SR3                | EclipseLink Persistence API                       
odl-base-gemini-web                   | 2.2.0.RELEASE       | x         | odl-base-1.4.5-Helium-SR3                | Gemini Web                                        
odl-base-tomcat                       | 7.0.53              | x         | odl-base-1.4.5-Helium-SR3                | OpenDaylight Tomcat                               
odl-base-spring                       | 3.1.3.RELEASE       | x         | odl-base-1.4.5-Helium-SR3                | Opendaylight Spring Support                       
odl-base-spring-web                   | 3.1.3.RELEASE       | x         | odl-base-1.4.5-Helium-SR3                | OpenDaylight Spring Web                           
odl-base-spring-security              | 3.1.3.RELEASE       | x         | odl-base-1.4.5-Helium-SR3                | OpenDaylight Spring Security                      
odl-tcpmd5-all                        | 1.0.3-Helium-SR3    |           | odl-tcpmd5-1.0.3-Helium-SR3              |                                                   
odl-tcpmd5-base                       | 1.0.3-Helium-SR3    |           | odl-tcpmd5-1.0.3-Helium-SR3              |                                                   
odl-tcpmd5-netty                      | 1.0.3-Helium-SR3    |           | odl-tcpmd5-1.0.3-Helium-SR3              |                                                   
odl-tcpmd5-nio                        | 1.0.3-Helium-SR3    |           | odl-tcpmd5-1.0.3-Helium-SR3              |                                                   
odl-sfc-all                           | 0.0.4-Helium-SR3    |           | odl-sfc-0.0.4-Helium-SR3                 | OpenDaylight :: sfc :: All                        
odl-sfc-provider                      | 0.0.4-Helium-SR3    |           | odl-sfc-0.0.4-Helium-SR3                 | OpenDaylight :: sfc :: Provider                   
odl-sfc-model                         | 0.0.4-Helium-SR3    |           | odl-sfc-0.0.4-Helium-SR3                 | OpenDaylight :: sfc :: Model                      
odl-sfc-test-consumer                 | 0.0.4-Helium-SR3    |           | odl-sfc-0.0.4-Helium-SR3                 | OpenDaylight :: sfc :: Test :: Consumer           
odl-sfc-ui                            | 0.0.4-Helium-SR3    |           | odl-sfc-0.0.4-Helium-SR3                 | OpenDaylight :: sfc :: UI                         
odl-mdsal-all                         | 1.1.3-Helium-SR3    |           | odl-mdsal-1.1.3-Helium-SR3               | OpenDaylight :: MDSAL :: All                      
odl-mdsal-broker                      | 1.1.3-Helium-SR3    | x         | odl-mdsal-1.1.3-Helium-SR3               | OpenDaylight :: MDSAL :: Broker                   
odl-toaster                           | 1.1.3-Helium-SR3    |           | odl-mdsal-1.1.3-Helium-SR3               | OpenDaylight :: Toaster                           
odl-mdsal-xsql                        | 1.1.3-Helium-SR3    |           | odl-mdsal-1.1.3-Helium-SR3               |                                                   
odl-mdsal-clustering-commons          | 1.1.3-Helium-SR3    |           | odl-mdsal-1.1.3-Helium-SR3               |                                                   
odl-mdsal-distributed-datastore       | 1.1.3-Helium-SR3    |           | odl-mdsal-1.1.3-Helium-SR3               |                                                   
odl-mdsal-remoterpc-connector         | 1.1.3-Helium-SR3    |           | odl-mdsal-1.1.3-Helium-SR3               |                                                   
odl-mdsal-clustering                  | 1.1.3-Helium-SR3    |           | odl-mdsal-1.1.3-Helium-SR3               |                                                   
odl-clustering-test-app               | 1.1.3-Helium-SR3    |           | odl-mdsal-1.1.3-Helium-SR3               |                                                   
odl-flow-model                        | 1.1.3-Helium-SR3    | x         | odl-flow-1.1.3-Helium-SR3                | OpenDaylight :: Flow :: Model                     
odl-flow-services                     | 1.1.3-Helium-SR3    | x         | odl-flow-1.1.3-Helium-SR3                | OpenDaylight :: Flow :: Services                  
odl-openflow-nxm-extensions           | 0.0.6-Helium-SR3    | x         | ovsdb-0.0.6-Helium-SR3                   | OpenDaylight :: Openflow :: Nicira Extensions     
odl-integration-compatible-with-all   | 0.2.3-Helium-SR3    |           | odl-integration-0.2.3-Helium-SR3         |                                                   
odl-integration-all                   | 0.2.3-Helium-SR3    |           | odl-integration-0.2.3-Helium-SR3         |                                                   
odl-openflowjava-all                  | 0.0.0               |           | odl-openflowjava-0.5.3-Helium-SR3        | OpenDaylight :: Openflow Java :: All              
odl-openflowjava-protocol             | 0.5.3-Helium-SR3    | x         | odl-openflowjava-0.5.3-Helium-SR3        | OpenDaylight :: Openflow Java :: Protocol         
odl-nsf-all                           | 0.4.5-Helium-SR3    | x         | nsf-0.4.5-Helium-SR3                     | OpenDaylight :: NSF :: All Network Service Functio
odl-nsf-managers                      | 0.4.5-Helium-SR3    | x         | nsf-0.4.5-Helium-SR3                     | OpenDaylight :: AD-SAL :: Network Service Function
odl-adsal-northbound                  | 0.4.5-Helium-SR3    | x         | nsf-0.4.5-Helium-SR3                     | OpenDaylight :: AD-SAL :: Northbound APIs         
odl-bgpcep-all                        | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-dependencies               | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-util                       | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-concepts                   | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-linkstate                  | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-pcep-impl                  | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-pcep-segment-routing              | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-parser                     | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-rib                        | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-tunnel                     | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-programming                | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-pcep-api                          | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-pcep-spi                          | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-bgpcep-topology                   | 0.3.4-Helium-SR3    |           | odl-bgpcep-0.3.4-Helium-SR3              |                                                   
odl-config-persister-all              | 0.2.8-Helium-SR3    |           | odl-config-persister-0.2.8-Helium-SR3    | OpenDaylight :: Config Persister:: All            
odl-config-persister                  | 0.2.8-Helium-SR3    | x         | odl-config-persister-0.2.8-Helium-SR3    | OpenDaylight :: Config Persister                  
odl-config-startup                    | 0.2.8-Helium-SR3    | x         | odl-config-persister-0.2.8-Helium-SR3    | OpenDaylight :: Config Persister:: Config Startup 
odl-protocol-framework                | 0.5.3-Helium-SR3    | x         | odl-protocol-framework-0.5.3-Helium-SR3  | OpenDaylight :: Protocol Framework                
odl-restconf-all                      | 1.1.3-Helium-SR3    |           | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: Restconf :: All                   
odl-restconf                          | 1.1.3-Helium-SR3    | x         | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: Restconf                          
odl-restconf-noauth                   | 1.1.3-Helium-SR3    | x         | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: Restconf                          
odl-mdsal-apidocs                     | 1.1.3-Helium-SR3    | x         | odl-controller-1.1.3-Helium-SR3          | OpenDaylight :: MDSAL :: APIDOCS                  
odl-toaster-rest                      | 1.1.3-Helium-SR3    |           | odl-controller-1.1.3-Helium-SR3          |                                                   
odl-toaster-ui                        | 1.1.3-Helium-SR3    |           | odl-controller-1.1.3-Helium-SR3          |                                                   
odl-yangtools-all                     | 0.6.5-Helium-SR3    |           | odl-yangtools-0.6.5-Helium-SR3           | OpenDaylight Yangtools All                        
odl-yangtools-models                  | 0.6.5-Helium-SR3    | x         | odl-yangtools-0.6.5-Helium-SR3           | OpenDaylight :: Yangtools :: Models               
odl-yangtools-data-binding            | 0.6.5-Helium-SR3    | x         | odl-yangtools-0.6.5-Helium-SR3           | OpenDaylight :: Yangtools :: Data Binding         
odl-yangtools-binding                 | 0.6.5-Helium-SR3    | x         | odl-yangtools-0.6.5-Helium-SR3           | OpenDaylight :: Yangtools :: Binding              
odl-yangtools-common                  | 0.6.5-Helium-SR3    | x         | odl-yangtools-0.6.5-Helium-SR3           | OpenDaylight :: Yangtools :: Common               
odl-yangtools-binding-generator       | 0.6.5-Helium-SR3    | x         | odl-yangtools-0.6.5-Helium-SR3           | OpenDaylight :: Yangtools :: Binding Generator    
odl-yangtools-restconf                | 0.6.5-Helium-SR3    |           | odl-yangtools-0.6.5-Helium-SR3           | OpenDaylight :: Yangtools :: Restconf             
odl-adsal-compatibility-all           | 1.4.5-Helium-SR3    |           | odl-adsal-compatibility-0.8.4-Helium-SR3 | OpenDaylight :: controller :: All                 
odl-adsal-compatibility               | 0.8.4-Helium-SR3    | x         | odl-adsal-compatibility-0.8.4-Helium-SR3 | OpenDaylight :: AD-SAL :: Compatibility           
odl-ovsdb-all                         | 1.0.3-Helium-SR3    |           | ovsdb-1.0.3-Helium-SR3                   | OpenDaylight :: OVSDB :: all                      
odl-ovsdb-library                     | 1.0.3-Helium-SR3    | x         | ovsdb-1.0.3-Helium-SR3                   | OVSDB :: Library                                  
odl-ovsdb-schema-openvswitch          | 1.0.3-Helium-SR3    | x         | ovsdb-1.0.3-Helium-SR3                   | OVSDB :: Schema :: Open_vSwitch                   
odl-ovsdb-schema-hardwarevtep         | 1.0.3-Helium-SR3    | x         | ovsdb-1.0.3-Helium-SR3                   | OVSDB :: Schema :: hardware_vtep                  
odl-ovsdb-plugin                      | 1.0.3-Helium-SR3    | x         | ovsdb-1.0.3-Helium-SR3                   | OpenDaylight :: OVSDB :: Plugin                   
odl-ovsdb-northbound                  | 0.6.3-Helium-SR3    | x         | ovsdb-1.0.3-Helium-SR3                   | OpenDaylight :: OVSDB :: Northbound               
odl-ovsdb-openstack                   | 1.0.3-Helium-SR3    | x         | ovsdb-1.0.3-Helium-SR3                   | OpenDaylight :: OVSDB :: OpenStack Network Virtual
odl-ovsdb-ovssfc                      | 0.0.4-Helium-SR3    |           | ovsdb-0.0.4-Helium-SR3                   | OpenDaylight :: OVSDB :: OVS Service Function Chai
odl-sfclisp                           | 0.0.4-Helium-SR3    |           | odl-sfclisp-0.0.4-Helium-SR3             | OpenDaylight :: sfclisp :: all                    
odl-sfcofl2                           | 0.0.4-Helium-SR3    |           | odl-sfcofl2-0.0.4-Helium-SR3             | OpenDaylight :: sfcofl2                           
odl-dlux-all                          | 0.1.3-Helium-SR3    |           | odl-dlux-0.1.3-Helium-SR3                |                                                   
odl-dlux-core                         | 0.1.3-Helium-SR3    | x         | odl-dlux-0.1.3-Helium-SR3                |                                                   
pax-cdi                               | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | Provide CDI support                               
pax-cdi-1.1                           | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | Provide CDI 1.1 support                           
pax-cdi-weld                          | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | Weld CDI support                                  
pax-cdi-1.1-weld                      | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | Weld CDI 1.1 support                              
pax-cdi-openwebbeans                  | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | OpenWebBeans CDI support                          
pax-cdi-web                           | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | Web CDI support                                   
pax-cdi-1.1-web                       | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | Web CDI 1.1 support                               
pax-cdi-web-weld                      | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | Weld Web CDI support                              
pax-cdi-1.1-web-weld                  | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | Weld Web CDI 1.1 support                          
pax-cdi-web-openwebbeans              | 0.7.0               |           | org.ops4j.pax.cdi-0.7.0                  | OpenWebBeans Web CDI support                      
pax-cdi-deltaspike-core               | >0.5                |           | org.ops4j.pax.cdi-0.7.0                  | Apache Deltaspike core support                    
pax-cdi-deltaspike-jpa                | 0.5                 |           | org.ops4j.pax.cdi-0.7.0                  | Apche Deltaspike jpa support                      
odl-vtn-manager-all                   | 0.2.3-Helium-SR3    |           | vtn-manager-0.2.3-Helium-SR3             | OpenDaylight VTN Manager All                      
odl-vtn-manager-java-api              | 0.2.3-Helium-SR3    |           | vtn-manager-0.2.3-Helium-SR3             | OpenDaylight :: VTN Manager :: Java API           
odl-vtn-manager-northbound            | 0.2.3-Helium-SR3    |           | vtn-manager-0.2.3-Helium-SR3             | OpenDaylight :: VTN Manager :: Northbound         
odl-vtn-manager-neutron               | 0.2.3-Helium-SR3    |           | vtn-manager-0.2.3-Helium-SR3             | OpenDaylight :: VTN Manager :: Neutron Interface  
odl-aaa-authz-all                     | 0.1.3-Helium-SR3    |           | odl-aaa-0.1.3-Helium-SR3                 | OpenDaylight :: AAA :: Authorization :: All Featur
odl-aaa-authz                         | 0.1.3-Helium-SR3    |           | odl-aaa-0.1.3-Helium-SR3                 | OpenDaylight :: AAA :: Authorization              
spring-dm                             | 1.2.1               |           | spring-3.0.1                             | Spring DM support                                 
spring-dm-web                         | 1.2.1               |           | spring-3.0.1                             | Spring DM Web support                             
spring                                | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x support                              
spring-aspects                        | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x AOP support                          
spring-instrument                     | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x Instrument support                   
spring-jdbc                           | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x JDBC support                         
spring-jms                            | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x JMS support                          
spring-struts                         | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x Struts support                       
spring-test                           | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x Test support                         
spring-orm                            | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x ORM support                          
spring-oxm                            | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x OXM support                          
spring-tx                             | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x Transaction (TX) support             
spring-web                            | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x Web support                          
spring-web-portlet                    | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring 3.1.x Web Portlet support                  
spring                                | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x support                              
spring-aspects                        | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x AOP support                          
spring-instrument                     | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x Instrument support                   
spring-jdbc                           | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x JDBC support                         
spring-jms                            | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x JMS support                          
spring-struts                         | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x Struts support                       
spring-test                           | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x Test support                         
spring-orm                            | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x ORM support                          
spring-oxm                            | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x OXM support                          
spring-tx                             | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x Transaction (TX) support             
spring-web                            | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x Web support                          
spring-web-portlet                    | 3.2.4.RELEASE       |           | spring-3.0.1                             | Spring 3.2.x Web Portlet support                  
spring                                | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x support                              
spring-aspects                        | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x AOP support                          
spring-instrument                     | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x Instrument support                   
spring-jdbc                           | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x JDBC support                         
spring-jms                            | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x JMS support                          
spring-test                           | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x Test support                         
spring-orm                            | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x ORM support                          
spring-oxm                            | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x OXM support                          
spring-tx                             | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x Transaction (TX) support             
spring-web                            | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x Web support                          
spring-web-portlet                    | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x Web Portlet support                  
spring-websocket                      | 4.0.2.RELEASE_1     |           | spring-3.0.1                             | Spring 4.0.x WebSocket support                    
spring-security                       | 3.1.4.RELEASE       |           | spring-3.0.1                             | Spring Security 3.1.x support                     
gemini-blueprint                      | 1.0.0.RELEASE       |           | spring-3.0.1                             | Gemini Blueprint Extender                         
odl-sdninterfaceapp-all               | 1.4.5-Helium-SR3    |           | odl-sdninterfaceapp-1.4.5-Helium-SR3     | OpenDaylight :: sdninterfaceapp                   
odl-lispflowmapping-all               | 1.1.14-Helium-SR3   |           | odl-lispflowmapping-1.1.14-Helium-SR3    | OpenDaylight :: LISP Flow Mapping :: All          
odl-lispflowmapping-mappingservice    | 1.1.14-Helium-SR3   |           | odl-lispflowmapping-1.1.14-Helium-SR3    | OpenDaylight :: LISP Flow Mapping :: Mapping Servi
odl-lispflowmapping-southbound        | 1.1.14-Helium-SR3   |           | odl-lispflowmapping-1.1.14-Helium-SR3    | OpenDaylight :: LISP Flow Mapping :: Southbound Pl
odl-lispflowmapping-northbound        | 1.1.14-Helium-SR3   |           | odl-lispflowmapping-1.1.14-Helium-SR3    | OpenDaylight :: LISP Flow Mapping :: Northbound   
odl-lispflowmapping-netconf           | 1.1.14-Helium-SR3   |           | odl-lispflowmapping-1.1.14-Helium-SR3    | OpenDaylight :: LISP Flow Mapping :: NETCONF      
odl-lispflowmapping-neutron           | 1.1.14-Helium-SR3   |           | odl-lispflowmapping-1.1.14-Helium-SR3    | OpenDaylight :: LISP Flow Mapping :: Neutron Integ
odl-akka-all                          | 1.4.5-Helium-SR3    |           | odl-controller-1.4.5-Helium-SR3          | OpenDaylight :: Akka :: All                       
odl-akka-scala                        | 2.10                |           | odl-controller-1.4.5-Helium-SR3          | Scala Runtime for OpenDaylight                    
odl-akka-system                       | 2.3.4               |           | odl-controller-1.4.5-Helium-SR3          | Akka Actor Framework System Bundles               
odl-akka-clustering                   | 2.3.4               |           | odl-controller-1.4.5-Helium-SR3          | Akka Clustering                                   
odl-akka-leveldb                      | 0.7                 |           | odl-controller-1.4.5-Helium-SR3          | LevelDB                                           
odl-akka-persistence                  | 2.3.4               |           | odl-controller-1.4.5-Helium-SR3          | Akka Persistence                                  
transaction                           | 1.0.1               | x         | enterprise-3.0.1                         | OSGi Transaction Manager                          
jpa                                   | 1.0.1               |           | enterprise-3.0.1                         | OSGi Persistence Container                        
openjpa                               | 2.2.2               |           | enterprise-3.0.1                         | Apache OpenJPA 2.2.x persistence engine support   
openjpa                               | 2.3.0               |           | enterprise-3.0.1                         | Apache OpenJPA 2.3.x persistence engine support   
hibernate                             | 3.3.2.GA            |           | enterprise-3.0.1                         | Hibernate 3.x JPA persistence engine support      
hibernate                             | 4.2.7.Final         |           | enterprise-3.0.1                         | Hibernate 4.2.x JPA persistence engine support    
hibernate-envers                      | 4.2.7.Final         |           | enterprise-3.0.1                         | Hibernate Envers 4.2.x                            
hibernate                             | 4.3.1.Final         |           | enterprise-3.0.1                         | Hibernate 4.3.x JPA persistence engine support    
hibernate-envers                      | 4.3.1.Final         |           | enterprise-3.0.1                         | Hibernate Envers 4.3.x                            
hibernate-validator                   | 5.0.3.Final         |           | enterprise-3.0.1                         | Hibernate Validator support                       
jndi                                  | 3.0.1               |           | enterprise-3.0.1                         | OSGi Service Registry JNDI access                 
jdbc                                  | 3.0.1               |           | enterprise-3.0.1                         | JDBC service and commands                         
jms                                   | 3.0.1               |           | enterprise-3.0.1                         | JMS service and commands                          
openwebbeans                          | 1.2.1               |           | enterprise-3.0.1                         | Apache OpenWebBeans CDI container support         
weld                                  | 2.1.1.Final         |           | enterprise-3.0.1                         | JBoss Weld CDI container support                  
application-without-isolation         | 1.0.0               |           | enterprise-3.0.1                         | Provide EBA archive support                       
odl-ttp-all                           | 0.0.4-Helium-SR3    |           | odl-ttp-0.0.4-Helium-SR3                 | OpenDaylight :: ttp :: All                        
odl-ttp-model                         | 0.0.4-Helium-SR3    |           | odl-ttp-0.0.4-Helium-SR3                 | OpenDaylight :: ttp :: Model                      
odl-netconf-all                       | 0.2.8-Helium-SR3    |           | odl-netconf-0.2.8-Helium-SR3             | OpenDaylight :: Netconf :: All                    
odl-netconf-api                       | 0.2.8-Helium-SR3    | x         | odl-netconf-0.2.8-Helium-SR3             | OpenDaylight :: Netconf :: API                    
odl-netconf-mapping-api               | 0.2.8-Helium-SR3    | x         | odl-netconf-0.2.8-Helium-SR3             | OpenDaylight :: Netconf :: Mapping API            
odl-netconf-util                      | 0.2.8-Helium-SR3    | x         | odl-netconf-0.2.8-Helium-SR3             |                                                   
odl-netconf-impl                      | 0.2.8-Helium-SR3    | x         | odl-netconf-0.2.8-Helium-SR3             | OpenDaylight :: Netconf :: Impl                   
odl-config-netconf-connector          | 0.2.8-Helium-SR3    | x         | odl-netconf-0.2.8-Helium-SR3             | OpenDaylight :: Netconf :: Connector              
odl-netconf-netty-util                | 0.2.8-Helium-SR3    | x         | odl-netconf-0.2.8-Helium-SR3             | OpenDaylight :: Netconf :: Netty Util             
odl-netconf-client                    | 0.2.8-Helium-SR3    |           | odl-netconf-0.2.8-Helium-SR3             | OpenDaylight :: Netconf :: Client                 
odl-netconf-monitoring                | 0.2.8-Helium-SR3    | x         | odl-netconf-0.2.8-Helium-SR3             | OpenDaylight :: Netconf :: Monitoring             
odl-snbi-all                          | 1.0.3-Helium-SR3    |           | odl-snbi-1.0.3-Helium-SR3                | OpenDaylight :: snbi :: All                       
odl-snbi-southplugin                  | 1.0.3-Helium-SR3    |           | odl-snbi-1.0.3-Helium-SR3                | OpenDaylight :: SNBI :: SouthPlugin               
odl-snbi-shellplugin                  | 1.0.3-Helium-SR3    |           | odl-snbi-1.0.3-Helium-SR3                | OpenDaylight :: SNBI :: ShellPlugin               
pax-jetty                             | 8.1.14.v20131031    | x         | org.ops4j.pax.web-3.1.0                  | Provide Jetty engine support                      
pax-tomcat                            | 7.0.27.1            |           | org.ops4j.pax.web-3.1.0                  | Provide Tomcat engine support                     
pax-http                              | 3.1.0               | x         | org.ops4j.pax.web-3.1.0                  | Implementation of the OSGI HTTP Service           
pax-http-whiteboard                   | 3.1.0               | x         | org.ops4j.pax.web-3.1.0                  | Provide HTTP Whiteboard pattern support           
pax-war                               | 3.1.0               | x         | org.ops4j.pax.web-3.1.0                  | Provide support of a full WebContainer            
odl-openflowplugin-all                | 0.0.6-Helium-SR3    |           | openflowplugin-0.0.6-Helium-SR3          | OpenDaylight :: Openflow Plugin :: All            
odl-openflowplugin-southbound         | 0.0.6-Helium-SR3    | x         | openflowplugin-0.0.6-Helium-SR3          | OpenDaylight :: Openflow Plugin :: SouthBound     
odl-openflowplugin-flow-services      | 0.0.6-Helium-SR3    | x         | openflowplugin-0.0.6-Helium-SR3          | OpenDaylight :: Openflow Plugin :: Flow Services  
odl-openflowplugin-flow-services-rest | 0.0.6-Helium-SR3    |           | openflowplugin-0.0.6-Helium-SR3          | OpenDaylight :: Openflow Plugin :: Flow Services :
odl-openflowplugin-flow-services-ui   | 0.0.6-Helium-SR3    |           | openflowplugin-0.0.6-Helium-SR3          | OpenDaylight :: Openflow Plugin :: Flow Services :
odl-openflowplugin-drop-test          | 0.0.6-Helium-SR3    |           | openflowplugin-0.0.6-Helium-SR3          | OpenDaylight :: Openflow Plugin :: Drop Test      
odl-openflowplugin-apps               | 0.0.6-Helium-SR3    |           | openflowplugin-0.0.6-Helium-SR3          | OpenDaylight :: Openflow Plugin :: Applications   
odl-groupbasedpolicy-ofoverlay        | 0.1.3-Helium-SR3    |           | odl-groupbasedpolicy-0.1.3-Helium-SR3    | OpenDaylight :: groupbasedpolicy :: OpenFlow Overl
"""
