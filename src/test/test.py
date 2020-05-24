
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, Date

Base = declarative_base()

# create table test (
#   test_id 		int not null auto_increment,
#   test_name 	varchar(32) not null,
#   test_date 	date default null,
#   test_value 	decimal(7,2) default null,
#   test_type		tinyint,
#   created		timestamp not null default current_timestamp,
#   primary key (test_id)
# );
# /** 如果是invisible，这样优化器就会忽略这个索引，但是索引依然存在于引擎内部 */
# ALTER TABLE test ADD INDEX idx_test_name (test_name ASC) VISIBLE;

class Test(Base):
    __tablename__ = 'test'
    test_id = Column(Integer, primary_key=True)
    test_name = Column(String)
    test_date = Column(DateTime)
    test_value = Column(DECIMAL)
    test_type = Column(Integer)
    created = Column(Date)