'use client';

import { useSystem } from '@context/useSystem';
import React from 'react';
import { FaHome, FaMedal, FaTrophy } from 'react-icons/fa';
import { GiSoccerBall, GiSoccerKick } from 'react-icons/gi';
import { IoFlag } from 'react-icons/io5';
import { MdStadium } from 'react-icons/md';

const Aside = () => {
  const { isAsideOpen, setIsAsideOpen }: any = useSystem();

  return (
    <div className="flex">
      <aside
        className={`px-[10px] pt-14 text-zinc-900 bg-white w-auto h-full fixed left-0 ${
          !isAsideOpen && 'transform translate-x-[-100%]'
        } z-30 transition-all shadow-[0px_1px_5px_1px_#00000024]`}
      >
        <ul className="pr-2 z-2 w-80 top-[50px]">
          <li className="aside-li">
            <a href="/">
              <div className="min-w-[50px] flex justify-center text-[30px] ">
                <FaHome />
              </div>
              <span>Home</span>
            </a>
          </li>
          <li className="aside-li">
            <a href="#">
              <div className="min-w-[50px] flex justify-center text-[30px] ">
                <FaMedal />
              </div>
              <span>Leagues</span>
            </a>
          </li>
          <li className="aside-li">
            <a href="#">
              <div className="min-w-[50px] flex justify-center text-[30px] ">
                <GiSoccerBall />
              </div>
              <span>Teams</span>
            </a>
          </li>
          <li className="aside-li">
            <a href="#">
              <div className="min-w-[50px] flex justify-center text-[30px] ">
                <GiSoccerKick />
              </div>
              <span>Players</span>
            </a>
          </li>
          <li className="aside-li">
            <a href="#">
              <div className="min-w-[50px] flex justify-center text-[30px] ">
                <IoFlag />
              </div>
              <span>Countries</span>
            </a>
          </li>
          <li className="aside-li">
            <a href="#">
              <div className="min-w-[50px] flex justify-center text-[30px] ">
                <MdStadium />
              </div>
              <span>Stadiums</span>
            </a>
          </li>
          <li className="aside-li">
            <a href="#">
              <div className="min-w-[50px] flex justify-center text-[30px] ">
                <FaTrophy />
              </div>
              <span>Trophies</span>
            </a>
          </li>
        </ul>
      </aside>

      <div
        onClick={() => {
          setIsAsideOpen(false);
        }}
        className={`overlay w-screen h-screen top-0 left-0 fixed z-20 bg-[#000000a4] ${
          !isAsideOpen && 'opacity-0 pointer-events-none'
        }`}
      ></div>
    </div>
  );
};

export default Aside;
