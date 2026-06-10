from sqlalchemy import Column, Integer, BigInteger, Float, Boolean, PrimaryKeyConstraint
from database import Base

class CleanTransactionData(Base):
    __tablename__ = 'transaction_data'
    __table_args__ = (
        PrimaryKeyConstraint('basket_id', 'product_id'),
        {'schema': 'clean'}
    )

    # Исходные ключи
    basket_id = Column(BigInteger, nullable=False)
    product_id = Column(Integer, nullable=False)

    # Основные поля транзакции
    household_key = Column(BigInteger, nullable=False, index=True)
    day = Column(Integer, nullable=False, index=True)
    quantity = Column(Integer, nullable=False)
    sales_value = Column(Float, nullable=False)
    store_id = Column(Integer, nullable=False, index=True)
    trans_time = Column(Integer, nullable=True)
    week_no = Column(Integer, nullable=False, index=True)

    # Дисконтные поля
    retail_disc = Column(Float, nullable=True)           # скидка магазина (обычно отрицательная)
    coupon_disc = Column(Float, nullable=True)           # скидка по купону (обычно отрицательная)
    coupon_match_disc = Column(Float, nullable=True)     # доп. скидка за совпадение купона

    # Вычисляемые поля
    unit_price = Column(Float, nullable=True)            # sales_value / quantity (если quantity>0)
    total_discount = Column(Float, nullable=True)        # retail_disc + coupon_disc + coupon_match_disc
    discount_rate = Column(Float, nullable=True)         # total_discount / (sales_value - total_discount) или доля от базовой цены

    # Флаги валидности внешних ключей
    product_valid = Column(Boolean, nullable=False, server_default='false')
    household_valid = Column(Boolean, nullable=False, server_default='false')

    # Флаг промо-транзакции
    has_discount = Column(Boolean, nullable=False, server_default='false')  # retail_disc !=0 OR coupon_disc !=0 OR coupon_match_disc !=0

    def __repr__(self):
        return f"<CleanTransactionData(basket={self.basket_id}, product={self.product_id})>"