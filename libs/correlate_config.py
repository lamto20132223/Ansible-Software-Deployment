correlate_config.py

- Tìm ra được  những config nào đã bị thay đổi
- Xem xét config change làm thành performance issue 
- Tương tác với các SolarWinds systems, servers, network management products khác 
1. Track server and application changes:
	- Nhận alerted khi configurations change 
	- -> Cần biết được thời điểm, vị tríconfig thay đổi và ai làm ra thay đổi 
	- Sử dụng agent-based monitoring trên Linux sẽ nhìn ra đc thay đổi trong thời gian thực và ai làm thay đổi tới file này 
	- configuration Detail:
	+ Last change Time 
	+ Last status check 
	+ configuration items 

2. Compare configuration changes over time:
	- Xác định những thay đổi giữa 2 version của 1 file, script output hoặc registry settings
	- Stop "stare and compare" với highlights the changes giữa 2 configuration versions 
3. Vẽ mối liên hệ giữa config change và performance
4. Quản lý tập chung các tập lệnh, phân phối các tập lệnh đó đến các máy chủ trong môi trường của bạn, sau đó theo dõi và cảnh báo về các thay đổi đối với toàn bộ đầu ra của các tập lệnh
	==> Mở rộng năng lực  giám sát tới level của scripting prowess

5. 
Unified Web-based Dashboard
	- Network Performance Monitor 
	- Netflow Traffic Analyzer
Discovery and Resource Mapping
	- Network Configuration Manager 
	- Virtualization Manager 
Contralized Settings and Access Control 
	- Server and Application Monitor 
Alerting and Reporting 
	- Storage Resource Monitor 
	- Database Performance Analyzer
Consolidated Metric and Data 
	- Log Manager For Orion 
	- Server Configuration Monitor


6. Bổ xung ansible-network lấy thông tin các con switch_