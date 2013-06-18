delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_get_reading`()
BEGIN
  select
	id,
	date,
	state
	from lectura
	where state = 1;
END$$

delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_ins_entry`(dt datetime, lip varchar(15), 
rip varchar(15), web varchar(1024))
BEGIN
	insert into log 
	(date,
	 localip,
	 remoteip,
	 url)
	values 
	(dt,
	 lip,
	 rip,
	 web); 
END$$

delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_ins_reading`(dt datetime)
BEGIN
	insert into lectura (date, state)
	values (dt, 1);
END$$


delimiter $$

CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_upd_reading`(cod int)
BEGIN
	update lectura
	set state = 0
	where id = cod;
END$$
























