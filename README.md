## Introduction

I work for Microsoft and spend 90% of my time on Cloud Networking. You won't find much code here, rather articles relating to the design and configuration of Azure Networking solutions and products. Checkout who I [follow](https://github.com/adstuart?tab=following) on GitHub for colleagues at Microsoft who publish similar content.

Connect with me: &nbsp; [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/adamstuart1) [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCRAegs4OmMFVGcU9tDBRlKg) [![Azure Networking Book](https://img.shields.io/badge/📘_Azure_Networking_Book-0078D4?style=for-the-badge)](https://azurenetworkingbook.com)

## Repo structure

| Category | Article | Year | Link |
|----------|---------|:----:|------|
| **P2S VPN** | Migrate from DirectAccess to Always On VPN with Azure Virtual WAN | 2021 | [Repo](https://github.com/adstuart/azure-vpn-p2s/tree/main/vwan-multihub) |
| | Migrate from DirectAccess to Always On VPN with Azure VPN Gateway | 2021 | [Repo](https://github.com/adstuart/azure-vpn-p2s/tree/main/vpngateway-multivnet) |
| | Azure VPN Client deployment via Intune | 2021 | [Repo](https://github.com/adstuart/azure-vpn-p2s/tree/main/intune-azurevpnclient) |
| | Optimising Azure VPN P2S costs using Intune and Windows 10 VPN autotrigger | 2021 | [Repo](https://github.com/adstuart/azure-vpn-p2s/tree/main/intune-win10-triggers) |
| | Windows 10 IKEv2 traffic selectors | 2021 | [Repo](https://github.com/adstuart/azure-vpn-p2s/tree/main/misc-win10-ikev2-trafficselectors) |
| | P2S command cheatsheet | 2021 | [Repo](https://github.com/adstuart/azure-vpn-p2s/tree/main/misc-cheatsheet) |
| | P2S custom routes | 2021 | [Repo](https://github.com/adstuart/azure-vpn-p2s/tree/main/custom-routes) |
| **PL** | Azure Private Link Governance using RBAC and Azure Policy | 2020 | [Repo](https://github.com/adstuart/azure-privatelink-policy) |
| | Using Azure Firewall as DNS Forwarder with Private Link | 2020 | [Repo](https://github.com/adstuart/azure-privatelink-dns-azurefirewall) |
| | Azure Private Link DNS MicroHack | 2020 | [Repo](https://github.com/adstuart/azure-privatelink-dns-microhack) |
| | DNS considerations for Multi-region use of Azure Private Link | 2021 | [Repo](https://github.com/adstuart/azure-privatelink-multiregion) |
| | Multi-region Private Link Service categories | 2022 | [Repo](https://github.com/adstuart/azure-privatelink-multiregion-services) |
| | Azure Site Recovery and Private Link DNS | 2022 | [Repo](https://github.com/adstuart/azure-privatelink-multiregion-siterecovery-asr) |
| | Using Azure Private Link with PartitionedDns enabled Azure Storage accounts | 2023 | [Repo](https://github.com/adstuart/-azure-privatelink-storage-dnsparition) |
| **VWAN** | Azure Virtual WAN BGP Peering - Anycast multi-region load balancing | 2021 | [Repo](https://github.com/adstuart/azure-vwan-anycast) |
| | Connect Cisco ASA to VWAN via IPsec VPN | 2022 | [Repo](https://github.com/adstuart/azure-vwan-asa) |
| | Azure Virtual WAN Route-Maps ASN guidance | 2023 | [Repo](https://github.com/adstuart/azure-vwan-routemaps-asn) |
| | VWAN default route scenarios | 2023 | [Repo](https://github.com/adstuart/azure-vwan-defaultroute) |
| | VWAN Forced tunnel over s2s VPN | 2023 | [Repo](https://github.com/adstuart/azure-vwan-s2s-forcedtunnel) |
| **Other** | Azure Networking Mindmap | 2019 | [Repo](https://github.com/adstuart/azurenetworkingmindmap/blob/master/Azure%20Networking%20Product%20Map%20V2.0.png) |
| | SD-WAN and Azure | 2022 | [Repo](https://github.com/adstuart/azure-sdwan) |
| | Beyond 500 Spoke VNets | 2022 | [Repo](https://github.com/adstuart/azure-vnet-beyond-500-spokes) |
| | ARS ESU Neworking guidance | 2023 | [Repo](https://github.com/adstuart/azure-arc-esu) |
| | VNet Flow Logs - Hub vs Spoke enablement considerations | 2024 | [Repo](https://github.com/adstuart/azure-vnetflowlogs-wheretoenable) |
| **S2S VPN** | High-security S2S VPN connectivity, Azure to 3rd parties | 2021 | [Repo](https://github.com/adstuart/azure-vpn-s2s/tree/main/3P-connectivity) |
| | Expected downtime when resizing VPN Gateway SKU | 2021 | [Repo](https://github.com/adstuart/azure-vpn-s2s/tree/main/resize-gateway) |
| | AS-path manipulation A/A VPN-GW | 2021 | [Repo](https://github.com/adstuart/azure-vpn-s2s/tree/main/active-active-aspath) |
| | Floating IP failover behaviour on VPN GW and VWAN | 2021 | [Repo](https://github.com/adstuart/azure-vpn-s2s/tree/main/failover-floating) |
| **ER** | ExpressRoute Migration Guide | 2021 | [Repo](https://github.com/adstuart/azure-expressroute-migration) |
| | Combining ExpressRoute Direct with ExpressRoute Local | 2021 | [Repo](https://github.com/adstuart/azure-expressroute-direct-local) |
| | ExpressRoute GlobalReach and AVS considerations | 2022 | [Repo](https://github.com/adstuart/azure-expressroute-globalreach-avs) |
| | ExpressRoute ECMP behaviour | 2023 | [Repo](https://github.com/adstuart/azure-expressroute-ecmp) |
| **ARS** | ARS summarisation | 2021 | [Repo](https://github.com/adstuart/azure-routeserver-summarisation) |
| | Azure Route Server and Anycast | 2021 | [Repo](https://github.com/adstuart/azure-routeserver-anycast) |
| | Azure Route Server + Infoblox | 2021 | [Repo](https://github.com/adstuart/azure-routeserver-infoblox) |
| | Azure Route Server MSEE transit gotchas | 2021 | [Repo](https://github.com/adstuart/azure-anycast-interregion) |
| **LB** | Azure Load Balancer hairpin | 2019 | [Repo](https://github.com/microsoft/Azure-ILB-hairpin) |
| | Cross-region private network load balancing in Azure | 2021 | [Repo](https://github.com/adstuart/azure-crossregion-private-lb) |
| | Azure Load Balancer Floating IP to On-Premises (or AVS) backend | 2021 | [Repo](https://github.com/adstuart/azure-dnat-floatingip-csr) |
| | Azure Gateway Load Balancer Service Chaining with HAPRoxy and Palo Alto | 2023 | [Repo](https://github.com/adstuart/azure-gwlb-chain) |
| **AI** | Azure AI Foundry Governance — Single vs Multi-Resource Architecture Decision | 2026 | [Repo](https://github.com/adstuart/azure-foundry-governance) |
| | Do I Need a WAF in Front of My AI Workload? | 2026 | [Repo](https://github.com/adstuart/do-i-need-a-waf-for-my-ai-workload) |
| **AZFW** | Stop/Start AZFW dataplane | 2021 | [Repo](https://github.com/adstuart/azure-firewall-deallocate) |
| | Customer-managed Public IPs at scale on AZFW in VWAN Hub | 2025 | [Repo](https://github.com/adstuart/azure-firewall-vwan-multipip) |
| **DNS** | Azure DNS Private Resolver topology options | 2023 | [Repo](https://github.com/adstuart/azure-resolver-topologyoptions) |

